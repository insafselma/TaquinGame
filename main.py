from Board import (
    GOAL_STATE,
    is_goal,
    get_successors,
    misplaced_tiles,
    f_cost
)

# Initial / scrambled state
initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

print("Initial state:")
print(initial_state)

print("Goal state:")
print(GOAL_STATE)

print("Is goal:", is_goal(initial_state))

# Calculate h(n)
h = misplaced_tiles(initial_state)

# For the initial node, g(n) = 0
g = 0

# Calculate f(n)
f = f_cost(g, h)

print("g(n) =", g)
print("h(n) =", h)
print("f(n) =", f)

# Generate successors
print("Successors:")
for successor in get_successors(initial_state):
    print(successor)
    