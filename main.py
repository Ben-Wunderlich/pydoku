import random
import copy
import MakePic
import sys

WIDTH = HEIGHT = 9
NUMS = {1,2,3,4,5,6,7,8,9}

def InitGrid():
    grid = []
    for _ in range(WIDTH):
        grid.append([])
        for _ in range(HEIGHT):
            grid[-1].append(0)
    return grid

def TakenNums(grid, x, y):
    taken = set()
    for i in range(WIDTH):
        taken.add(grid[i][x])
        taken.add(grid[y][i])

    x3 = x//3
    y3 = y//3

    for yi, row in enumerate(grid):
        for xi, el in enumerate(row):
            if(xi//3 == x3 and yi//3 == y3):
                taken.add(el)
    return taken

def GetSquare(grid, x, y):
    possibilities = copy.deepcopy(NUMS)
    taken = TakenNums(grid, x, y)
    possibilities -= taken

    if len(possibilities) == 0:
        return -1

    return random.choice(list(possibilities))


def FillGrid(grid):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            el = GetSquare(grid, x, y)
            if el == -1:
                return -1
            grid[y][x] = el

    return 0            


def ShowGrid(arr):
    for y, row in enumerate(arr):
        for x, item in enumerate(row):
            if(item == -1):
                print("_ ", end="")
            else:
                #print("\033[4m" + str(item)+" ", end="\033[0m")
                print(item,"", end="")

            if(x != 8 and (x%3) == 2):
                print("  ", end="")
        if(y!= 8 and (y%3) == 2):
            print()
        print()
    print()

def RemoveNum(grid):
    x = random.randint(0,8)
    y = random.randint(0,8)
    if(grid[y][x] == -1):
        return -1
    grid[y][x] = -1
    return 0

def RemoveNums(grid, remaining=5):
    newGrid = copy.deepcopy(grid)
    limit = 81-remaining
    taken = 0
    while taken < limit:
        if RemoveNum(newGrid) == 0:
            taken+=1
    return newGrid


def GetFilledGrid():
    result = -1
    while result == -1:
        grid = InitGrid()
        result = FillGrid(grid)
    return grid

def strIsInt(givenStr):
    try: 
        int(givenStr)
        return True
    except ValueError:
        return False

def main():
    print("Starting page generation\n")

    numPages = 1
    if len(sys.argv) > 1 and strIsInt(sys.argv[1]):
        numPages = int(sys.argv[1])

    remaining = 40
    if len(sys.argv) > 2 and strIsInt(sys.argv[2]) and int(sys.argv[2]) <= 81:
        remaining = int(sys.argv[2])

    for _ in range(numPages):

        gridSolved = GetFilledGrid()
        gridUnsolved = RemoveNums(gridSolved, remaining)


        grid2Solved = GetFilledGrid()
        grid2Unsolved = RemoveNums(grid2Solved, remaining)

        #pagenum could be from either
        MakePic.MakePage(gridUnsolved, grid2Unsolved, False)#make puzzle page
        pagenum = MakePic.MakePage(gridSolved, grid2Solved, True)#make solution page

        print("Finished page", pagenum)

    print("\nFinished all pages, now exiting")

if __name__ == "__main__":
    main()