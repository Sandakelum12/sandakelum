import random

cross_section_photo_effect = 0.8  # Material properties as a percent
cross_section_scattering = 0.2   # Material properties


n_simulating_incidents = 100000 # Simulation parameter which means how many times simulating

# Counter for photoelectric and scattering events from 0 to 1
n_photo = 0
n_scatter = 0


for i in range(n_simulating_incidents):
    # Generate a random number between 0 and 1
    r = random.random()

    # Compare the random number to the probability of the photoelectric effect
    if r < cross_section_photo_effect / (cross_section_photo_effect + cross_section_scattering):
        n_photo += 1

    else:
        n_scatter += 1
        
print(r)
   
# Print the results       
print("Number of photoelectric events:", n_photo)
print("Number of scattering events:", n_scatter)





