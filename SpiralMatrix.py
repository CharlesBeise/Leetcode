def spiralOrder(matrix):
    # Initialize border numbers
    left = 0
    right = len(matrix[0])
    up = 1
    down = len(matrix)

    # Create variables for managing the final result
    result = []
    targetLen = right * down

    i = 0
    j = 0

    while len(result) < targetLen:
        # Add numbers moving right
        while j < right:
            result.append(matrix[i][j])
            j += 1
        right -= 1
        j -= 1
        i += 1

        # Add numbers moving down
        while i < down:
            result.append(matrix[i][j])
            i += 1
        down -= 1
        i -= 1
        j -= 1

        # Add numbers moving left
        while j >= left:
            result.append(matrix[i][j])
            j -= 1
        left += 1
        j += 1
        i -= 1

        # Add numbers moving up
        while i >= up:
            result.append(matrix[i][j])
            i -= 1
        up += 1
        i += 1
        j += 1

    # If the matrix is a rectangle instead of a square, it will incorrectly
    # backtrack along the last line. This removes the incorrectly added items
    while len(result) > targetLen:
        result.pop()

    return result


if __name__ == '__main__':
    testMatrix = [[1,2], [3, 4], [5, 6]]
    print(spiralOrder(testMatrix))


"""
Keep track of decreasing "border numbers"
There are 4 phases:
- Move right
- Move down
- Move left
- Move up
Once each phase is complete, decrease the border number for that direction by 1
"""