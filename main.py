from Solver import a_star

# Initial state
initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Run A*
solution = a_star(initial_state)

# Display the solution
print("Solution:")

for state in solution:
    print(state)
    print()
    