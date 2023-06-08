def naiveCountNegatives(grid):
    total = 0
    for row in grid:
        for col in row:
            if col < 0:
                total += 1

    return total

def countNegatives(grid):
    rows = len(grid)
    cols = len(grid[0])

    cur = 0
    total = 0

    for i in range(rows - 1, -1, -1):
        while cur < cols and grid[i][cur] >= 0:
            cur += 1
        total += (cols - cur)

    return total


if __name__ == '__main__':
    myGrid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(countNegatives(myGrid))