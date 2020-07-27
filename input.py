def inputFile(filename, mode):
    maze = []
    try:
        with open(filename, mode) as f:
            # Input size
            size = int(f.readline())

            # Input maze
            for _ in range(size * size):
                d = f.readline()
                maze.append(list(map(int, d.split())))

            # Input goal
            goal = int(f.readline())

    except IOError as err:
        print(err)

    return maze, goal
