import math
import matplotlib.pyplot as plt
import random
import numpy as np


no_of_incident = np.random.randint(1,101,100)


photo_percent = int(len(no_of_incident)/2) # 100/2 = 50; 5% of 100
scatter_percent = int(len(no_of_incident)/2) # 100/2 = 50; 5% of 100


photo_percent_list = random.sample(list(no_of_incident), photo_percent) #<class 'list'>
scatter_percent_list = random.sample(list(no_of_incident), scatter_percent) #<class 'list'>

np_incident_photo = np.array(photo_percent_list) #<class 'numpy.ndarray'>
np_incident_sacatter = np.array(scatter_percent_list) #<class 'numpy.ndarray'>

random_selected_photo_count=len(np_incident_photo)
random_selected_scatter_count=len(np_incident_sacatter)

#print(photo_percent)
print(f"photo effect:{np_incident_photo}")
print(f"scattering:{np_incident_sacatter}")

print(f"photo effect:{random_selected_photo_count}")
print(f"scattering:{random_selected_scatter_count}")

np_incident_photo = np.array(photo_percent_list) #<class 'numpy.ndarray'>
#np_incident_sacatter = np.array(scatter_percent_list)
plt.scatter(np_incident_photo, np_incident_sacatter, color = 'hotpink')

#x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
#y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
#plt.scatter(x, y, color = '#88c999')

plt.show()
