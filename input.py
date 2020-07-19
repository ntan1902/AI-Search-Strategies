def inputFile(filename, mode):
    try:
        f = open(filename, mode)
    except IOError as err:
        print(err)

    size = int(f.readline())
    maze = []

    for _ in range(size*size):
        d = f.readline()
        maze.append(list(map(int, d.split())))
    goal = int(f.readline())
    f.close()
    return maze, goal
