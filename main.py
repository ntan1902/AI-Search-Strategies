import input
import search
import sys
if __name__ == '__main__':
    """Initialize maze, goal"""
    if len(sys.argv) != 2:
        file = input.inputFile("INPUT/Maze5x5.txt", "r")
    else:
        print(sys.argv[1])
        file = input.inputFile(sys.argv[1], "r")
    maze = file[0]
    goal = file[1]
    start = 0
    maxDepth = len(maze)

    print("============ Breadth First Search ================")
    path_bfs, explored_bfs = search.BFS(maze, start, goal)
    print(f"Explored nodes: {explored_bfs}")
    if len(path_bfs) > 0:
        print(f"Path: {path_bfs}")
        print(f"Time to escape the maze: {len(explored_bfs)}")
    else:
        print("No solution")
    print()


    print("============ Uniform Cost Search ================")
    path_ucs, explored_ucs = search.UCS(maze, start, goal)
    print(f"Explored nodes: {explored_ucs}")
    if len(path_ucs) > 0:
        print(f"Path: {path_ucs}")
        print(f"Time to escape the maze: {len(explored_ucs)}")
    else:
        print("No solution")
    print()


    print("============ Iterative Deepening Search ================")
    path_ids, explored_ids = search.IDS(maze, start, goal, maxDepth)
    time_escape = 0
    for i in range(len(explored_ids)):
        print(f"Explored nodes in depth {i}: {explored_ids[i]}")
        time_escape += len(explored_ids[i])

    if len(path_ids) > 0:
        print(f"Path: {path_ids}")
        print(f"Time to escape the maze: {time_escape}")
    else:
        print("No solution")
    print()


    print("============ Greedy-Best First Search ================")
    path_gbfs, explored_gbfs = search.Greedy_BFS(maze, start, goal)
    print(f"Explored nodes: {explored_gbfs}")
    if len(path_gbfs) > 0:
        print(f"Path: {path_gbfs}")
        print(f"Time to escape the maze: {len(explored_gbfs)}")
    else:
        print("No solution")
    print()

    print("============ A* Search ================")
    path_a, explored_a = search.Tree_A(maze, start, goal)
    print(f"Explored nodes: {explored_a}")
    if len(path_a) > 0:
        print(f"Path: {path_a}")
        print(f"Time to escape the maze: {len(explored_a)}")
    else:
        print("No solution")
    print()