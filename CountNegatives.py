def countNegatives(grid):
    total = 0
    for row in grid:
        for col in row:
            if col < 0:
                total += 1

    return total


if __name__ == '__main__':
    myGrid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(countNegatives(myGrid))