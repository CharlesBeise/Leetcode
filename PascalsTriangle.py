def generate(numRows):
    triangle = []

    for i in range(1, numRows + 1):
        newRow = [1 for _ in range(i)]
        for j in range(1, i - 1):
            newRow[j] = triangle[i - 2][j - 1] + triangle[i - 2][j]
        triangle.append(newRow)

    return triangle


if __name__ == '__main__':
    testRows = 5
    print(generate(testRows))
