#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def SolveMaze(m, s, g):
    # check if the current location is the goal
    if s == g:
        m[s[0]][s[1]] = 'P'  # mark the path with 'P'
        print_maze(m)  # print the maze with the path
        return True
    
    # check if the current location is valid and not already visited
    if not is_valid(m, s):
        return False
    
    # mark the current location as visited
    m[s[0]][s[1]] = 'P'
    
    # explore the four cardinal directions recursively
    if SolveMaze(m, (s[0]-1, s[1]), g):  # north
        return True
    if SolveMaze(m, (s[0], s[1]+1), g):  # east
        return True
    if SolveMaze(m, (s[0]+1, s[1]), g):  # south
        return True
    if SolveMaze(m, (s[0], s[1]-1), g):  # west
        return True
    
    # if none of the directions lead to the goal, backtrack and mark the current location as unvisited
    m[s[0]][s[1]] = '0'
    return False

def is_valid(m, s):
    # check if the current location is within the maze bounds
    if s[0] < 0 or s[0] >= len(m) or s[1] < 0 or s[1] >= len(m[0]):
        return False
    # check if the current location is not blocked or already visited
    if m[s[0]][s[1]] == '1' or m[s[0]][s[1]] == 'P':
        return False
    # check if the current location is not adjacent to the current path
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 'P' and abs(r-s[0])+abs(c-s[1]) == 1:
                return False
    return True

def print_maze(m):
    for row in m:
        print(' '.join(row))
    print()

'''Solve maze testing file and opening the txts provided'''
with open('maze.txt') as f:
    maze = [list(line.strip()) for line in f.readlines()]

start = (0, 0)
goal = (5, 7)

SolveMaze(maze, start, goal)
