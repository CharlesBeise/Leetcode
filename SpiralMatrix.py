def spiralOrder(matrix):
    left = 0
    right = len(matrix[0])
    up = 1
    down = len(matrix)
    result = []
    targetLen = right * down

    i = 0
    j = 0

    while len(result) < targetLen:
        while j < right:
            result.append(matrix[i][j])
            j += 1
        right -= 1
        j -= 1
        i += 1

        while i < down:
            result.append(matrix[i][j])
            i += 1
        down -= 1
        i -= 1
        j -= 1

        while j >= left:
            result.append(matrix[i][j])
            j -= 1
        left += 1
        j += 1
        i -= 1

        while i >= up:
            result.append(matrix[i][j])
            i -= 1
        up += 1
        i += 1
        j += 1

    while len(result) > targetLen:
        result.pop()

    return result


if __name__ == '__main__':
    testMatrix = [[1,2], [3, 4], [5, 6]]
    print(spiralOrder(testMatrix))


"""
Keep track of a decreasing "border numbers"
There are 4 phases:
- Move right
- Move down
- Move left
- Move up
Once each phase is complete, decrease the border number for that direction by 1
"""