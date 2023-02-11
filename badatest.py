import random
import math
energy = random.uniform(10**3, 10**6)
number_of_atoms = 1000
sigma = 200

print("Source_Energy : " , energy)

leave_energy_percentage = 50/100
photo_effect_percentage = 30/100
scatter_percentage = ((100/100)-(leave_energy_percentage+photo_effect_percentage))

Leave_energy =leave_energy_percentage*energy
print("Leave Energy : ",Leave_energy)

Photo_effect = photo_effect_percentage*energy
print("Photo Effect : ",Photo_effect)

Scatter = scatter_percentage*energy
print("Scatter : ",Scatter)

angle0_percentage = 40/100
angle1_89_percentage = 30/100
angle90_percentage = 15/100
angle91_179_percentage = 10/100
angle180_percentage = 5/100

angle0 = Scatter * angle0_percentage
print("Angle 0 : ",angle0)

angle1_89 = Scatter * angle1_89_percentage
print("Angle 1 - 89 : ",angle1_89)

angle90 = Scatter * angle90_percentage
print("Angle 90 : ",angle90)

angle91_179 = Scatter * angle91_179_percentage
print("Angle 91 - 179 : ",angle91_179)

angle180 = Scatter * angle180_percentage
print("Angle 180 : ",angle180)

energy = Photo_effect

while (Photo_effect>1000.0):
    print("======================================")
    print("Energy : " , energy)

    leave_energy_percentage = 50/100
    photo_effect_percentage = 30/100
    scatter_percentage = ((100/100)-(leave_energy_percentage+photo_effect_percentage))

    Leave_energy =leave_energy_percentage*energy
    print("Leave Energy : ",Leave_energy)

    Photo_effect = photo_effect_percentage*energy
    print("Photo Effect : ",Photo_effect)

    Scatter = scatter_percentage*energy
    print("Scatter : ",Scatter)

    angle0 = Scatter * angle0_percentage
    print("Angle 0 : ",angle0)

    angle1_89 = Scatter * angle1_89_percentage
    print("Angle 1 - 89 : ",angle1_89)

    angle90 = Scatter * angle90_percentage
    print("Angle 90 : ",angle90)

    angle91_179 = Scatter * angle91_179_percentage
    print("Angle 91 - 179 : ",angle91_179)

    angle180 = Scatter * angle180_percentage
    print("Angle 180 : ",angle180)
        
    energy = Photo_effect

path = (-(math.log(energy))/(number_of_atoms*sigma) )
#print("path : " , path)
