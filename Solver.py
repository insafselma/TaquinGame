from  Board import is_goal, get_successors, misplaced_tiles, f_cost
def a_star(start_state):
    states = [start_state]                              # les damiers découverts
    g_costs = [0]                                       # g de chaque damier
    f_costs = [f_cost(0, misplaced_tiles(start_state))] # f de chaque damier
    parents = [-1]                                      # numéro du parent de chaque damier
    open_list = [0]                                     # numéros des damiers à explorer
    closed_list = []                                    # damiers déjà explorés
#on cherche le damier avec le plus petit f 
    while len(open_list) > 0:
        best_index = open_list[0]
        for index in open_list:
            if f_costs[index] < f_costs[best_index]:
                best_index = index
        open_list.remove(best_index)
        current_state = states[best_index]

        if current_state not in closed_list:
            closed_list.append(current_state)
            g = g_costs[best_index]
            h = misplaced_tiles(current_state)
# si c'est le but je remonte les parents ( pour les afficher avec l interface)

            if is_goal(current_state):
                path = []
                node_index = best_index
                while node_index != -1:
                    path.append(states[node_index])
                    node_index = parents[node_index]
                path.reverse()
                return path

           #on crée les voisins du damier qui ne sont pas encore explorés 
            for successor in get_successors(current_state):
                if successor not in closed_list:
                    states.append(successor)
                    g_costs.append(g + 1)
                    f_costs.append(f_cost(g + 1, misplaced_tiles(successor)))
                    parents.append(best_index)
                    open_list.append(len(states) - 1)

    return []  
