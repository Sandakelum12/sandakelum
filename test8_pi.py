import random

# Number of points to generate
n = 1000

# Counter for points inside quarter-circle
count = 0

for i in range(n):
    # Generate random x and y values between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check if point is inside quarter-circle
    if x*x + y*y <= 1:
        count += 1

# Estimate value of pi
pi_estimate = 4 * (count / n)

print("Estimated value of pi:", pi_estimate)
