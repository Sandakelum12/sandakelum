import random
import matplotlib.pyplot as plt
import numpy as np

no_of_incident = int(input("please enter the size : "))

def List_function(n):
    list_array = []
    for i in range(n+1):
        list_array.append(i)
    return(list_array)

no_of_incident_list = List_function(no_of_incident)

random.shuffle(no_of_incident_list)  

#percentage = int(input("please enter the percentage: "))
percentage_1 = int(no_of_incident*(50/100))
percentage_2 = int((no_of_incident-percentage_1)*(30/100))

#print(percentage)

x = no_of_incident_list[0:percentage_1]
y = no_of_incident_list[percentage_2:no_of_incident]

#if percentage == x:
    

photo_effect = len(x)
print (f"photo effect count:{photo_effect}")
print("-----------------------------")

scattering = len(y)
print (f"scattering count:{scattering}")
print("-------------------------")


print(f"photo incident:{x}")
print("--------------------------")

print(f"scatter incident:{y}")

#plt.scatter(x, y, color = '#88c999')
#plt.bar(x,y,color = 'green')

#plt.plot(z, x, color = '#88c999')
#plt.plot(z, y, color = '#88c999')
#plt.show()