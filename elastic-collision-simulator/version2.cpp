#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct particle {
    double mass;
    double x;
    double velocity;
};

double time_to_collision(particle a, particle b) {
    if (a.velocity <= b.velocity) return 1e9;
    return (b.x - a.x) / (a.velocity - b.velocity);
}

void collide(particle &a, particle &b, double e) {
    double m1 = a.mass, m2 = b.mass;
    double u1 = a.velocity, u2 = b.velocity;

    double v1 = (m1*u1 + m2*u2 - m2*e*(u1-u2)) / (m1+m2);
    double v2 = (m1*u1 + m2*u2 + m1*e*(u1-u2)) / (m1+m2);

    a.velocity = v1;
    b.velocity = v2;
}

int main() {

    // you can now vary the amount of particles

    int n;
    cout << "Enter number of particles: ";
    cin >> n;

    float e;
    cout << "Enter the value of restitution (0-1): ";
    cin >> e;

    vector<particle> particles;

    for (int i = 0; i < n; i++) {
        particle p;

        cout << "\nParticle " << i << ":\n";
        cout << "Mass: ";
        cin >> p.mass;

        cout << "Position (x): ";
        cin >> p.x;

        cout << "Velocity: ";
        cin >> p.velocity;

        particles.push_back(p);
    }

    double time = 0.0;

    // i have realised since the last version that there can be multiple collisions, i have fixed the logic here
    for (int step = 0; step < 100; step++) {

        double min_time = 1e9;
        int collision_index = -1;

        // finding next collision
        for (int i = 0; i < particles.size() - 1; i++) {
            double t = time_to_collision(particles[i], particles[i + 1]);

            if (t < min_time) {
                min_time = t;
                collision_index = i;
            }
        }

        // when there are no collisions
        if (collision_index == -1 || min_time == 1e9) {
            cout << "\nNo more collisions.\n";
            break;
        }

        // move time
        time += min_time;

        cout << "\nTime: " << time << endl;
        cout << "Collision between particle "
             << collision_index << " and "
             << collision_index + 1 << endl;

        // moving all the particles
        for (auto &p : particles) {
            p.x += p.velocity * min_time;
        }

        cout << "At collision:\n";
        for (int i = 0; i < particles.size(); i++) {
            cout << "Particle " << i
                 << " | x = " << particles[i].x
                 << " | v = " << particles[i].velocity << endl;
        }

        // apply the collisions, the restitution is the same for all collisions
        collide(particles[collision_index],
                particles[collision_index + 1],
                e);

        cout << "After collision:\n";

        // reparsing the order of the particles
        sort(particles.begin(), particles.end(), [](particle a, particle b) {
            return a.x < b.x;
        });

        for (int i = 0; i < particles.size(); i++) {
            cout << "Particle " << i
                 << " | x = " << particles[i].x
                 << " | v = " << particles[i].velocity << endl;
        }
    }

    return 0;
}
