import random
#import matplotlib.pyplot as plt

cross_section_photo_effect =5  # Material properties as a percent
cross_section_scattering = 3 # Material properties 
n_leave_prob =2  #Material properties  as a percent


n_simulating_incidents = 10000  # Simulation parameter which means how many times simulating 

# Counter for photoelectric and scattering events from 0
n_photo = 0
n_scatter = 0
n_leave=0

for r in range(n_simulating_incidents):
    # Generate a random number between 0 and 100
    r = random.random()

    # Compare the random number to the probability of the photoelectric effect
    if r < cross_section_photo_effect / (cross_section_photo_effect + cross_section_scattering+n_leave_prob):
        n_photo += 1
        
    elif r > cross_section_scattering / (cross_section_photo_effect + cross_section_scattering+n_leave_prob):
        n_scatter += 1
        
    else:
        n_leave += 1
        
   
# Print the results       
print("Number of photoelectric events:", n_photo)
print("Number of scattering events:", n_scatter)
print("Number of scattering events:", n_leave)




#x=n_photo
#y=n_scatter
#plt.plot(x,y, color = '#88c999')
#plt.show()

