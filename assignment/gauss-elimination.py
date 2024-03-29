import numpy as np

# Function to take equation input from user
def input_equation(num_vars, equation_num):
    print(f"Enter coefficients for equation {equation_num} (separated by spaces, e.g., x1 y1 z1):")
    coefficients_input = input().split()
    
    # Check if the input is valid
    if len(coefficients_input) != num_vars:
        print(f"Invalid input! Please enter {num_vars} coefficients.")
        return input_equation(num_vars, equation_num)
    
    # Convert input to floats
    coefficients = [float(val) for val in coefficients_input]
    
    print(f"Enter constant for equation {equation_num}:")
    constant = float(input())
    
    # Display equation for confirmation
    print(f"You entered equation {equation_num}: {coefficients} = {constant}")
    
    return coefficients + [constant]

# Number of variables
num_vars = 3

# Input equations from user
print("Enter the coefficients for each equation one by one in the format x1 y1 z1, x2 y2 z2, etc.:")
equations = [input_equation(num_vars, i+1) for i in range(num_vars)]

# Create coefficient matrix (A) and constant matrix (B)
A = np.array([equation[:-1] for equation in equations])
B = np.array([equation[-1] for equation in equations])

# Augmented matrix
AB = np.column_stack((A, B))

# Gauss elimination method
n = len(B)
for i in range(n):
    # Make the diagonal elements 1
    if AB[i][i] == 0:
        print("Divide by zero error!")
        break
    AB[i] = AB[i] / AB[i][i]
    
    # Make the other elements in the column zero
    for j in range(i+1, n):
        AB[j] = AB[j] - AB[j][i] * AB[i]

# Back substitution
X = np.zeros(n)
for i in range(n-1, -1, -1):
    X[i] = AB[i][n]
    for j in range(i+1, n):
        X[i] -= AB[i][j] * X[j]

# Print the solution
print("\n### Solution: Determining the Costs of Three Different Items ###\n")
print("The unique prices of the items are:")
print("T-shirt (x) =", X[0])
print("Pair of jeans (y) =", X[1])
print("Jacket (z) =", X[2])
