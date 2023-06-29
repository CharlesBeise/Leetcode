def generate(rowIndex):
    newRow = [1]

    for i in range(1, rowIndex + 1):
        oldRow = newRow
        newRow = [1]
        for j in range(1, i):
            newRow.append(oldRow[j - 1] + oldRow[j])
        newRow.append(1)

    return newRow


if __name__ == '__main__':
    testRows = 6
    print(generate(testRows))
