# Simple CLI DOOM-inspired 3D engine
![Screenshot 2025-05-29 at 02 19 26](https://github.com/user-attachments/assets/79c114f9-7d92-4923-a3e6-c6a3b4889efc)

A simple, terminal-based 3D raycasting engine inspired by DOOM, written in Python using the curses library.
## Features
- First-person ASCII rendering of walls with distance shading
- Real-time movement using `WASD` controls
- Player field-of-view (FOV) and angle-based rendering
I tried to make a simply enemy but it didn't really work
Same goes for the gun HUD that I tried to make
My initial objective was to replicate DOOM entirely, but after an hour or so I realised that this goal was a tad too ambitious for now; so I simply opted to just create a system where the user can traverse around a 3D plane (similair to DOOM).

## Limitations
It is a very minamilistic project, so there are some limitations that could definitely be fixed if I decide to yet again pursue this project later down the line.
- No textures, lighting, or colours
- ASCII-only visualisation
- No AI logic
- Pretty much only serves to allow the player to roam a map
- 
## Requirements
- Python 3.6+
- Unix-like terminal with `curses` support (Linux/macOS)

## Limitations
- No textures, lighting, or 3D objects
- ASCII-only visualization
- Single enemy and no AI logic
