# JPMORGAN-Optimization-
Aim
To find the value of x that minimizes the energy function using derivative-based optimization.
General Objective
To apply mathematical optimization techniques to robotic energy management problems and understand the use of calculus-based methods for identifying optimal operating points.
Specific Objective
Synthetic Optimization Function
Source: Kaggle
#Procedure
Define the energy function
Compute derivative of the function
Set derivative equal to zero
Solve for x
Compute minimum energy
Display result
#Algorithm
Start
Define function 
Compute derivative
Set derivative = 0
Solve for x
Calculate minimum energy
Display result
Stop
Code Logic
# derivative = 0 → 2x - 6 = 0 → x = 3
Python Code
# Optimization: Finding Minimum Energy

def energy(x):
    return x**2 - 6*x + 10

def derivative(x):
    return 2*x - 6

# Solve derivative = 0
x = 3

# Calculate minimum energy
min_energy = energy(x)

print("Minimum point x =", x)
print("Minimum Energy E(x) =", min_energy)
Output
Minimum point x = 3
Minimum Energy E(x) = 1
Result
The minimum energy occurs at:
x = 3
E(x) = 1
Industry Application
Optimization is used in:
Robotics energy management
AI operations
Financial systems
Companies like JPMorgan Chase use optimization for:
Risk reduction
Resource allocation
Efficient decision-making
Conclusion
The minimum value of the energy function is successfully determined using derivative-based optimization, demonstrating the importance of calculus in solving real-world problems.
