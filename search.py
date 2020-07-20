import sys
import math
max_possible_value = sys.maxsize

def Greedy_BFS(maze, start, goal):
    path = []
    explored = []
    if start == goal:
        return path, explored

    path.append(start)

    path_cost = get_manhattan_heuristic(maze, start, goal)
    frontier = []
    frontier.append((path_cost, path))

    while len(frontier) > 0:
        # Pop frontier
        path_cost_now, path_till_now = pop_frontier(frontier)

        current_node = path_till_now[-1]

        # Push to explored
        explored.append(current_node)

        # Check node is goal
        if current_node == goal:
            return path_till_now, explored


        childs = maze[current_node]

        # Process neighbors in increasing order
        childs.sort()

        for child in childs:
            # Open child path
            path_to_child = path_till_now.copy()
            path_to_child.append(child)

            # Update new cost
            path_new_cost = get_manhattan_heuristic(maze, child, goal)
            new_path_child = (path_new_cost, path_to_child)

            # Check if child node exists in frontier
            child_is_in_frontier, position, path_old_cost = get_child_frontier(child, frontier)

            if (child not in explored) and not child_is_in_frontier:
                # Push into frontier
                frontier.append(new_path_child)
    return path, explored

def BFS(maze, start, goal):
    path = []
    explored = []
    if start == goal:
        return path, explored

    path.append(start)

    frontier = []
    frontier.append(path)

    while len(frontier) > 0:
        #Pop frontier
        path_till_now = frontier[0]
        frontier.pop(0)

        #Push to explored
        current_node = path_till_now[-1]
        explored.append(current_node)
        childs = maze[current_node]

        #Process neighbors in increasing order
        childs.sort()

        for child in childs:
            #Open child path
            path_to_child = path_till_now.copy()
            path_to_child.append(child)

            if (child not in explored) and (child not in frontier):
                #if find goal then update path and return
                if child == goal:
                    path_till_now.append(child)
                    return path_till_now, explored

                #else update push into frontier
                frontier.append(path_to_child)
    return path, explored

def UCS(maze, start, goal):
    path = []
    explored = []
    if start == goal:
        return path, explored

    path.append(start)

    path_cost = 0
    frontier = []
    frontier.append((path_cost, path))

    while len(frontier) > 0:
        # Pop frontier
        path_cost_now, path_till_now = pop_frontier(frontier)

        current_node = path_till_now[-1]

        # Push to explored
        explored.append(current_node)

        #Check node is goal
        if current_node == goal:
            return path_till_now, explored


        childs = maze[current_node]

        # Process neighbors in increasing order
        childs.sort()

        for child in childs:
            #Open child path
            path_to_child = path_till_now.copy()
            path_to_child.append(child)

            #Update new cost
            path_new_cost = 1 + path_cost_now
            new_path_child = (path_new_cost, path_to_child)

            #Check if child node exists in frontier
            child_is_in_frontier, position, path_old_cost = get_child_frontier(child, frontier)

            if (child not in explored) and not child_is_in_frontier:
                #Push into frontier
                frontier.append(new_path_child)

            elif child_is_in_frontier:
                if path_new_cost < path_old_cost:
                    frontier.pop(position)
                    frontier.append(new_path_child)
    return path, explored

def IDS(maze, start, goal, maxDepth):
    path = []
    explored = []
    for limit in range(maxDepth):
        if(DLS(maze, start, goal, 0, path, explored, limit)):
            path.append(start)
            path.reverse()
            return path, explored
    return path, explored

def DLS(maze, start, goal, parent, path, explored, limit):
    explored.append(start)
    if start == goal:
        return True
    if limit == 0:
        return False
    childs = maze[start]
    childs.sort()

    for child in childs:
        if child != parent:
            #Start node is now a parent of child
            find_goal = DLS(maze, child, goal, start, path, explored, limit - 1)
            if find_goal == True:
                path.append(child)
                return True
    return False

def pop_frontier(frontier):
    min = max_possible_value

    #Storing the paths having min cost
    paths = []

    for cost, path in frontier:
        if cost == min:
            paths.append(path)
        if cost < min:
            min = cost
            paths.clear()
            paths.append(path)

    #Sort the last element of each path
    paths = sorted(paths, key=lambda x: x[-1])

    path_res = paths[0]
    frontier.remove((min, paths[0]))

    return min, path_res

def get_child_frontier(child, frontier):
    for i in range(len(frontier)):
        cost, path = frontier[i]
        if path[-1] == child:
            return True, i, cost
    return False, None, None

def get_manhattan_heuristic(maze, start, goal):
    #8x8
    size_maze =  int(math.sqrt(len(maze)))

    j_start, i_start = divmod(start, size_maze)
    j_goal, i_goal = divmod(goal, size_maze)

    i_delta = abs(i_goal - i_start)
    j_delta = abs(j_goal - j_start)
    return i_delta + j_delta