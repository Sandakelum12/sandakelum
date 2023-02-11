import random
import numpy as np
import math


# Number of particles to simulate
n = 1000

# Material properties
absorption_probability = 0.1
scattering_probability = 0.9

# Initial position and direction of particles
particles = np.zeros((n,7))
particles[:,0:3] = np.random.rand(n,3)*10
particles[:,3:6] = np.random.rand(n,3)
particles[:,6] = np.random.rand(n)*100

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
        particles[i,3:6] = (math.cos(phi) * sin_theta, math.sin(phi) * sin_theta, cos_theta)
        
        # Move the particle a certain distance in the new direction
        distance = random.expovariate(1)
        particles[i,0:3] += distance * particles[i,3:6]

# print the result
print("Fraction of particles absorbed:", absorbed/n)

# Plotting the particle distribution
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(particles[:,0], particles[:,1], particles[:,2], c=particles[:,6], cmap='viridis')
plt.show()
