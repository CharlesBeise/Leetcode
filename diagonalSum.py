def diagonalSum(mat):
    j = len(mat)
    total = 0
    for i in range(j):
        total += mat[i][i] + mat[i][j - i - 1]

    if j % 2 == 1:
        mid = j // 2
        total -= mat[mid][mid]

    return total


if __name__ == '__main__':
    myMat = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(diagonalSum(myMat))

"""
Iterate through the list and add the numbers at either end of each list, 
working in towards the middle.

If the length of the list is odd, subtract the middle number from the total
(the Free space) because it should only be added once.
"""
