import input
import search

if __name__ == '__main__':
    """Initialize maze, goal"""
    file = input.inputFile("input.txt", "r")
    maze = file[0]
    goal = file[1]
    start = 0
    maxDepth = 14


    print("============ BFS Search ================")
    path_bfs, explored_bfs = search.BFS(maze, start, goal)
    print(f"Time to escape the maze: {len(explored_bfs)}")
    print(f"Explored nodes: {explored_bfs}")
    print(f"Path: {path_bfs}")

    print("============ UCS Search ================")
    path_ucs, explored_ucs = search.UCS(maze, start, goal)
    print(f"Time to escape the maze: {len(explored_ucs)}")
    print(f"Explored nodes: {explored_ucs}")
    print(f"Path: {path_ucs}")

    print("============ IDS Search ================")
    path_ids, explored_ids = search.IDS(maze, start, goal, maxDepth)
    print(f"Time to escape the maze: {len(explored_ids)}")
    print(f"Explored nodes: {explored_ids}")
    print(f"Path: {path_ids}")