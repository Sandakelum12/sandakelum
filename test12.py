import random
import math

# Number of particles to simulate
n = 10000

# Material properties
absorption_probability = 0.1
scattering_probability = 0.9

# Initial position and direction of particles
x = 0
y = 0
z = 0
direction = (1, 0, 0)

# Number of particles absorbed
absorbed = 0

for i in range(n):
    # Generate a random number to decide if the particle is absorbed or scattered
    event = random.uniform(0, 1)
    if event < absorption_probability:
        # Particle is absorbed
        absorbed += 1
    else:
        # Particle is scattered
        # Generate new direction using isotropic scattering
        phi = random.uniform(0, 2 * 3.14)
        cos_theta = random.uniform(-1, 1)
        sin_theta = math.sqrt(1 - cos_theta**2)
        direction = (math.cos(phi) * sin_theta, math.sin(phi) * sin_theta, cos_theta)
        
        # Move the particle a certain distance in the new direction
        distance = random.expovariate(1)
        x += distance * direction[0]
        y += distance * direction[1]
        z += distance * direction[2]

# print the result
print("Fraction of particles absorbed:", absorbed/n)
