def equalPairs(grid):
    # Make two dictionaries to contain the rows and columns of the grid
    rows = {}
    cols = {}

    def addElem(item, container):
        """Helper function used to add an item to a dictionary. A new entry
        will be created if the element is not yet in the dictionary."""
        if item in container:
            container[item] = container[item] + 1
        else:
            container[item] = 1


    # Populate the row and column dictionaries
    for i in range(len(grid)):
        rowString = ''.join(str(num) + '.' for num in grid[i])
        addElem(rowString, rows)
        colString = ''
        for j in range(len(grid[0])):
            colString += str(grid[j][i]) + '.'
        addElem(colString, cols)

    # Compare the two dictionaries and count the duplicates between them
    duplicates = 0
    for key in cols:
        if key in rows:
            duplicates += (cols[key] * rows[key])

    return duplicates


if __name__ == '__main__':
    myGrid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(myGrid))
