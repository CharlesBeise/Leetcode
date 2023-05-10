def generateMatrix(n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    left, top = 0, 0
    right, bottom = n, n
    cur = 1

    for i in range((n*2) - 1):
        # Moving right
        if i % 4 == 0:
            for j in range(left, right):
                result[top][j] = cur
                cur += 1
            right -= 1

        # Moving down
        elif i % 4 == 1:
            for j in range(top + 1, bottom):
                result[j][right] = cur
                cur += 1
            bottom -= 1

        # Moving left
        elif i % 4 == 2:
            for j in range(right - 1, left - 1, -1):
                result[bottom][j] = cur
                cur += 1
            left += 1

        # Moving up
        else:
            for j in range(bottom - 1, top, -1):
                result[j][left - 1] = cur
                cur += 1
            top += 1

    return result


if __name__ == '__main__':
    print(generateMatrix(4))
