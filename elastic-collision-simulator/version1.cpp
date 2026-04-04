/* 
OUTPUT
Before:
Particle0 | x = 0 | velocity = 5
Particle1 | x = 10 | velocity = -2

Time to collision: 1.42857

At collision:
Particle 0 | x = 7.14286 | velocity = 5
Particle 1 | x = 7.14286 | velocity = -2

After collision:
Particle0 | x = 7.14286 | velocity = -3.4
Particle1 | x = 7.14286 | velocity = 2.2
*/
#include <iostream>
#include <vector>
using namespace std;

struct particle {
    double mass; // mass of each particle, necessary to use in equations
    double x; // position, not necessary in written questions
    double velocity; // velocity of each particle, necessary to use in equations
};

double time_to_collision(particle a, particle b) {
    if (a.velocity <= b.velocity) return 1e9; // too slow to reach particle b, will never reach
    return (b.x - a.x) / (a.velocity - b.velocity); // returns the time it would take to reach particle b
}

void collide(particle &a, particle &b, double e) {
    double m1 = a.mass, m2 = b.mass; // initialising the masses
    double u1 = a.velocity, u2 = b.velocity; // initialising the velocities (before collision)

    double v1 = (m1*u1 + m2*u2 - m2*e*(u1-u2)) / (m1+m2);  // initialising velocity of particle "a" (after collision)
    double v2 = (m1*u1 + m2*u2 + m1*e*(u1-u2)) / (m1+m2); // initialising velocity of particle "b" (after collision)

    a.velocity = v1;
    b.velocity = v2;
}

int main() {
    vector<particle> particles;
    // creating 2 particles, setting their mass, position and velocity.
    particles.push_back({1.0, 0.0, 5.0});
    particles.push_back({2.0, 10.0, -2.0});
    // A particle of mass 1kg travelling at 5ms^-1 and a particle of mass 2kg travelling at 2ms^-1 in the opposite direction
    // It is assumed the particles are travelling on a smooth, frictionless plane thus their velocities will only ever change due to collision.

    cout << "Before:\n";
    
    for (int i = 0; i < particles.size(); i++) {
        cout << "Particle" << i
        << " | x = " << particles[i].x
        << " | velocity = " << particles[i].velocity << endl;
    }

    double t = time_to_collision(particles[0], particles[1]);
    cout << "\nTime to collision: " << t << endl;

    // moving particles to the collision point

    for (auto &p : particles) {
        p.x += p.velocity * t;
    }
    
    cout << "\nAt collision:\n";
    for (int i = 0; i < particles.size(); i++) {
        cout << "Particle " << i
        << " | x = " << particles[i].x
        << " | velocity = " << particles[i].velocity << endl;
    }

    // collision logic
    collide(particles[0], particles[1], 0.8); // calling the collision function, setting restitution as 0.8

    cout << "\nAfter collision:\n";

    for (int i = 0; i < particles.size(); i++) {
        cout << "Particle" << i
            << " | x = " << particles[i].x
            << " | velocity = " << particles[i].velocity << endl;
    }

    return 0;
}
