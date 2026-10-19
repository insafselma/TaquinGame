# Defining the Goal Board n0
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)
# Testing the goal state 
def is_goal(state):
    return state == GOAL_STATE
# empty square searching
def find_empty(state):
    return state.index(0)
# finding possible moves :
def get_possible_moves(empty_index):
    moves = []
    
    row = empty_index // 3
    col = empty_index % 3

    if row > 0:
        moves.append("UP")

    if row < 2:
        moves.append("DOWN")

    if col > 0:
        moves.append("LEFT")

    if col < 2:
        moves.append("RIGHT")

    return moves
# defining succesor to return possible states 
def get_successors(state):
    successors = []

    empty_index = find_empty(state)
    possible_moves = get_possible_moves(empty_index)

    directions = {
        "UP": -3,
        "DOWN": 3,
        "LEFT": -1,
        "RIGHT": 1
    }

    for move in possible_moves:
        new_state = list(state)

        tile_index = empty_index + directions[move]

        new_state[empty_index], new_state[tile_index] = (
            new_state[tile_index],
            new_state[empty_index]
        )

        successors.append(tuple(new_state))

    return successors

# defining the heuristic function 
def misplaced_tiles(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1

    return count
# defining the evaluation function
def f_cost(g, h):
    return g + h

