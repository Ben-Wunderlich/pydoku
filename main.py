import random
import copy
import MakePic

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
    limit = 81-remaining
    taken = 0
    while taken < limit:
        if RemoveNum(grid) == 0:
            taken+=1

def GetFilledGrid():
    result = -1
    while result == -1:
        grid = InitGrid()
        result = FillGrid(grid)
    return grid

def main():
    #grid = InitGrid()
    remaining = 40

    grid = GetFilledGrid()
    print("SOLVED")
    ShowGrid(grid)
    RemoveNums(grid, remaining)
    #print("UNSOLVED")
    #ShowGrid(grid)

    grid2 = GetFilledGrid()
    print("SOLVED")
    ShowGrid(grid2)
    RemoveNums(grid2, remaining)
    #print("got here")
    MakePic.main(grid, grid2, 1)


if __name__ == "__main__":
    main()