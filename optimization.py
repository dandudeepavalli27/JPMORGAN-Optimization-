# SESSION 7 – Optimization (Finding Minimum Energy)

# Step 1: Define energy function
def energy(x):
    return x**2 - 6*x + 10

# Step 2: Define derivative function
def derivative(x):
    return 2*x - 6

# Step 3: Solve derivative = 0
# 2x - 6 = 0 → x = 3
x = 3

# Step 4: Calculate minimum energy
min_energy = energy(x)

# Step 5: Display results
print("Minimum point x =", x)
print("Minimum Energy E(x) =", min_energy)

print("\nProgram Executed Successfully")
