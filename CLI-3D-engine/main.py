import math
import curses
import random

world_map = [
    "########",
    "#      #",
    "#  ##  #",
    "#   1  #",
    "########"
]

player_x = 4.0
player_y = 3.0
player_angle = 0.0

enemy_x = 2.0
enemy_y = 2.0

def get_shade(distance):
    if distance < 1: return '█'
    elif distance < 2: return '▓'
    elif distance < 3: return '▒'
    elif distance < 4: return '░'
    else: return '.'

def cast_ray(px, py, angle, world_map, max_depth=16):
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    for depth in range(1, max_depth * 10):
        depth /= 10.0
        x = int(px + cos_a * depth)
        y = int(py + sin_a * depth)
        if y < 0 or y >= len(world_map) or x < 0 or x >= len(world_map[0]):
            return max_depth
        if world_map[y][x] == '#':
            return depth
    return max_depth

def render_scene(stdscr):
    global player_x, player_y, player_angle
    height, width = stdscr.getmaxyx()
    fov = math.pi / 3
    for col in range(min(width, 120)):
        ray_angle = player_angle - fov / 2 + fov * col / width
        distance = cast_ray(player_x, player_y, ray_angle, world_map)
        wall_height = int(height / (distance + 0.1))
        shade = get_shade(distance)
        for row in range(height):
            try:
                if height // 2 - wall_height // 2 <= row <= height // 2 + wall_height // 2:
                    stdscr.addch(row, col, shade)
                elif row < height // 2:
                    stdscr.addch(row, col, ' ')
                else:
                    stdscr.addch(row, col, '.')
            except curses.error:
                continue
    gun_str = " --[]-- "
    for i, char in enumerate(gun_str):
        try:
            stdscr.addch(height - 2, width // 2 - len(gun_str)//2 + i, char)
        except curses.error:
            continue

    dx = enemy_x - player_x
    dy = enemy_y - player_y
    angle_to_enemy = math.atan2(dy, dx)
    angle_diff = (angle_to_enemy - player_angle + math.pi) % (2 * math.pi) - math.pi

    if abs(angle_diff) < fov / 2:
        dist = math.hypot(dx, dy)
        col = int((angle_diff + fov / 2) / fov * width)
        enemy_height = int(height / (dist + 0.1))
        for i in range(enemy_height):
            try:
                stdscr.addch(height // 2 - i, col, 'X')
            except curses.error:
                continue

def move_player(key):
    global player_x, player_y, player_angle
    step = 0.1
    if key == ord('a'):
        player_angle -= 0.1
    elif key == ord('d'):
        player_angle += 0.1
    elif key == ord('w'):
        new_x = player_x + math.cos(player_angle) * step
        new_y = player_y + math.sin(player_angle) * step
        if world_map[int(new_y)][int(new_x)] != '#':
            player_x, player_y = new_x, new_y
    elif key == ord('s'):
        new_x = player_x - math.cos(player_angle) * step
        new_y = player_y - math.sin(player_angle) * step
        if world_map[int(new_y)][int(new_x)] != '#':
            player_x, player_y = new_x, new_y

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(30)

    while True:
        stdscr.clear()
        render_scene(stdscr)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        move_player(key)

curses.wrapper(main)
