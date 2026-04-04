#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

struct particle {
    double mass;
    double x;
    double velocity;
    sf::Color color; // i found that its hard to see which ball changes direction during the simulations, each ball will be assigned their own colour
};

int main() {
    srand(time(0));
    int n;
    cout << "Enter number of particles: ";
    cin >> n;

    float e;
    cout << "Enter a value for the coefficient of restitution (0-1): ";
    cin >> e;

    vector<particle> particles;

    for (int i = 0; i < n; i++) {
        particle p;

        cout << "\nParticle" << i << "\n";
        cout << "Mass: ";
        cin >> p.mass;

        cout << "Position (x): ";
        cin >> p.x;

        cout << "Velocity: ";
        cin >> p.velocity;

        p.color = sf::Color(
            rand() % 256,
            rand() % 256,
            rand() % 256
        );

        particles.push_back(p);
    }

    // more efficient sort
    sort(particles.begin(), particles.end(), [](const particle &a, const particle &b) {
        return a.x < b.x;
    });

    sf::RenderWindow window(sf::VideoMode(sf::Vector2u(800, 800)), "COLLISION SIMULATION");

    float scale = 20.0f;
    float dt = 0.01f;

    sf::CircleShape circle(10);
    circle.setOrigin(sf::Vector2f(10.f, 10.f));

    while (window.isOpen()) {
        // event handling, i was trying to use code for sfml 2 for this for an hour and it didn't work
        while (auto event = window.pollEvent()) {
            if (event->is<sf::Event::Closed>())
                window.close();
        }
        // moving particles
        for (auto &p : particles) {
            p.x += ((p.velocity)/60) * dt;
        }
        //colizione
        for (int i = 0; i < particles.size() - 1; i++) {
            if (particles[i].x >= particles[i + 1].x &&
                particles[i].velocity > particles[i + 1].velocity) {

                double m1 = particles[i].mass;
                double m2 = particles[i + 1].mass;
                double u1 = particles[i].velocity;
                double u2 = particles[i + 1].velocity;

                cout << "\nCollision between particle "<< i << " and " << i + 1 << endl;
                cout << "Before: velocity of particle no." << i << " = " << u1 << ", velocity of particle no." << i+1 << " = " << u2 << endl;

                double v1 = (m1*u1 + m2*u2 - m2*e*(u1-u2)) / (m1+m2);
                double v2 = (m1*u1 + m2*u2 + m1*e*(u1-u2)) / (m1+m2);

                particles[i].velocity = v1;
                particles[i + 1].velocity = v2;

                cout << "After: velocity of particle no." << i << " = " << v1 << ", velocity of particle no." << i << " = " << v2 << endl;

                particles[i].x = particles[i + 1].x - 0.1;
            }
        }
        // render the particles
        window.clear();
        for (auto &p : particles) {
            circle.setFillColor(p.color);
            circle.setPosition(sf::Vector2f(p.x * scale, 100.f));
            window.draw(circle);
        };

        window.display();
    };

    return 0;
}
