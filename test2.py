import numpy as np
import matplotlib.pyplot as plt

def scatter_angle(energy, mass, theta):
    # Calculate the momentum of the particle
    momentum = np.sqrt(2 * energy * mass)

    # Calculate the scattering angle using the formula
    phi = np.arctan(theta / momentum)

    return phi

def detect_gamma_rays(energies, thicknesses, atomic_numbers):
    # Define the mass of a gamma ray
    mass = 662.0

    # Loop through the energies
    for energy in energies:
        # Calculate the scattering angle
        theta = 0.1
        phi = scatter_angle(energy, mass, theta)

        # Calculate the transmission of gamma rays through the atomic layers
        transmission = 1.0
        for i in range(len(thicknesses)):
            Z = atomic_numbers[i]
            t = thicknesses[i]
            transmission *= np.exp(-Z * t / np.sin(phi))

        # Plot the transmission vs. energy
        plt.plot(energy, transmission, 'ro')

    # Label the axes and show the plot
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Transmission')
    plt.show()

# Example inputs
energies = np.linspace(1, 10, 100) # 100 gamma ray energies from 1 MeV to 10 MeV
thicknesses = [0.01, 0.02, 0.03] # Thicknesses of 3 atomic layers
atomic_numbers = [14, 8, 26] # Atomic numbers of the elements in the 3 layers

# Call the detect_gamma_rays function
detect_gamma_rays(energies, thicknesses, atomic_numbers)
