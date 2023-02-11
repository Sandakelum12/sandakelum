import random


num_simulation = 10000

num_rolls = 10

results = []
for i in range(num_simulation):
    dice_sum = 0
    
for j in range(num_rolls):
    dice_sum = + random.randint(1, 6)
        
results.append(dice_sum)
average_sum = sum(results)/num_simulation

print(f"Avg dice roll sum over {num_simulation} simulations:{average_sum}")
