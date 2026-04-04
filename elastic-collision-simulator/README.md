# A C++ program that simulates Elastic Collisions In One Dimensions

As of creating this project, I'm a year 12 student studying A-level Further Maths, one of the modules being Further Mechanics. Chapter 4 of the Edexcel Further Mechanics Book (Elastic Collisions In One Dimensions) talks about questions involving the conservation of momentum and restitution. I often find that the questions given are always confusing up until I draw out a diagram visualising the question.

What better way to conceptualise such questions but to build a program in C++ that simulates such collision questions?

The most recent model of this simulation:
-
<img width="1317" height="432" alt="Screenshot 2026-04-05 at 00 28 24" src="https://github.com/user-attachments/assets/873b877d-3d7d-4042-8048-2284612fbb5f" />

The program uses equations that are detailed in the specific chapter within the Edexcel Further Mechanics Book, such as:
m1u1 + m2u2 = m1v1 + m2v2 (Conservation of momentum)
and
e = (v2-v1)/(u1-u2) (Equation of the coefficient of restitution.
These equations are applied during each collision to update particle velocities.

The program:
- Simulates multiple particles moving in one dimension
- Detects collisions between particles
- Applies conservation of momentum and restitution
- Updates velocities after each collision
- Provides a visual representation using SFML

Current Features
- 
- Real time particle movement
- Adjustable number of particles
- Custom mass, position (as in the order of the particles), and velocity inputs
- Configurable coefficient of restitution
- Console logging of collision events

Future Improvements
-
- Add the ability to configure walls and boundaries
- Improve collision accuracy (event based timing)
- Display particle data (mass, velocity) visually
- Add pause/step through functionality
- Refactor into a modular simulation engine

Requirements
-
To run this project locally, you will need:
- A **C++** compiler (*e.g, clang++ or g++*)
- **SFML** (version 3.x recommended)
- Linux, macOS, or Windows

Installation (Linux)
-
On Debian/Ubuntu based distros:
`
sudo apt update
sudo apt install libsfml-dev
`
On Arch Linux:
`
sudo pacman -S sfml
`

Installation (macOS)
- 
If you are using macOS with **Homebrew**:
`
brew install sfml
`

Installation (Windows)
-
Install [vcpkg](https://vcpkg.io/), then run:
`
vcpkg install sfml
`
You can also download SFML manually and configure the include and library paths yourself I believe.

Compiling & Running (Linux)
-
Navigate to the project folder:
`
cd /path/to/project
`
Compile:
`
g++ -std=c++17 main.cpp -o sim \ 
-lsfml-graphics -lsfml-window -lsfml-system
`
Run:
`
./sim
`

Compiling & Running (macOS):
-
Navigate to the project folder:
`
cd /path/to/project
`
Compile:
`
clang++ -std=c++17 main.cpp -o sim \
-I$(brew --prefix sfml)/include \
-L$(brew --prefix sfml)/lib \
-lsfml-graphics -lsfml-window -lsfml-system
`
Run:
`
./sim
`

Compiling & Running (Windows):
-
If you are using MSYS2 WinGW or a compiler setup where SFML is already linked correctly, compile with:
`
g++ -std=c++17 main.cpp -o sim.exe -lsfml-graphics -lsfml-window -lsfml-system
`
Run:
`
.\sim.exe
`
If you are using Visual Studio, you will need to configure:
- C/C++ include directories
- linker library directories
- SFML `.lib` files
- required `.dll` files for runtime

Example Usage
-
When the program runs, you will be prompted to enter:
- Number of particles
- Coefficient of restitution (0-1)
- For each particle: Mass, Initial Position and Velocity.

**Example input:**

Enter number of particles: 2
Enter a value for the coefficient of restitution (0-1): 1

Particle 0
Mass: 1
Position (x): 0
Velocity: 5

Particle 1
Mass: 1
Position (x): 10
Velocity: -5
