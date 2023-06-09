def solveSudoku(board):
    # Find the center of each of the 9 sub-boxes
    subSquares = [(a, b) for a in [1, 4, 7] for b in [1, 4, 7]]

    # Create a dictionary to contain all the missing values fore each row,
    # column, and sub-square
    remaining = {"rows": {r : set() for r in range(9)},
                 "cols": {c: set() for c in range(9)},
                 "squares": {s : set() for s in subSquares}}
    
    nums = {str(i) for i in range(1, 10)}
    unsolved = 0

    # Find the missing numbers in each row and column and store this in 
    # the "remaining" dictionary
    for cur in range(len(board)):
        remaining["rows"][cur] = nums.difference(set(board[cur]))

        curCol = set()
        for i in range(9):
            if board[i][cur] != '.':
                curCol.add(board[i][cur])
            else:
                unsolved += 1

        remaining["cols"][cur] = nums.difference(curCol)
    

    # Find the missing numbers in each sub-square and store this in the
    # "remaining" dictionary
    for coord in subSquares:
        x, y = coord
        curSquare = set()
        adjacent = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        for neighbor in adjacent:
            val = board[x - neighbor[0]][y - neighbor[1]]
            if val != '.':
                curSquare.add(val)
        remaining["squares"][coord] = nums.difference(curSquare)


    """Now helper functions are used to solve the sudoku."""

    def placeNumber(location, sector, value):
        """This method is called when a number is entered into a cell on the board"""
        board[location[0]][location[1]] = value
        remaining["squares"][sector].remove(value)
        remaining["rows"][location[0]].remove(value)
        remaining["cols"][location[1]].remove(value)


    def undoNumber(location, sector, value):
        """This method is called whenever an entry needs to be undone"""
        board[location[0]][location[1]] = '.'
        remaining["squares"][sector].add(value)
        remaining["rows"][location[0]].add(value)
        remaining["cols"][location[1]].add(value)


    def solver(board, remaining, unsolved):
        """This method searches the board to see if a number can be placed"""
        if unsolved == 0:
            return board
        
        bestGuess = [(9, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9], (9, 9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # Identify in which sub-square the empty space is located
                    if i % 3 == 0:
                        x = i + 1
                    elif i % 3 == 1:
                        x = i
                    else:
                        x = i - 1

                    if j % 3 == 0:
                        y = j + 1
                    elif j % 3 == 1:
                        y = j
                    else:
                        y = j - 1

                    candidates = remaining["squares"][(x, y)].intersection(remaining["rows"][i])
                    candidates = candidates.intersection(remaining["cols"][j])

                    # If only 1 candidate remains, then it may be placed in the cell
                    if len(candidates) == 1:
                        candidate = list(candidates)[0]
                        placeNumber((i, j), (x, y), candidate)
                        continuation = solver(board, remaining, unsolved - 1)
                        if continuation:
                            return board
                        undoNumber((i, j), (x, y), candidate)
                        return False
                    elif len(candidates) < len(bestGuess[1]):
                        bestGuess = [(i, j), candidates, (x, y)]
                    # If there are no valid candidates, then an error has been made and we need to backtrack
                    # and change the incorrect assumption
                    elif len(candidates) == 0:
                        return False
                    

        # If the board has been iterated through and no cell was filled, we need to make a 
        # best guess and see if it is valid
        cell, candidates, square = bestGuess
        curCand = 0
        candidates = list(candidates)
        while curCand < len(candidates):
            placeNumber(cell, square, candidates[curCand])
            attempt = solver(board, remaining, unsolved - 1)
            if attempt:
                return board
            undoNumber(cell, square, candidates[curCand])
            curCand += 1

        return False
                

    return solver(board, remaining, unsolved)


if __name__ == '__main__':
    # unsolved = 54
    myBoard = [[".",".","9","7","4","8",".",".","."],
               ["7",".",".",".",".",".",".",".","."],
               [".","2",".","1",".","9",".",".","."],
               [".",".","7",".",".",".","2","4","."],
               [".","6","4",".","1",".","5","9","."],
               [".","9","8",".",".",".","3",".","."],
               [".",".",".","8",".","3",".","2","."],
               [".",".",".",".",".",".",".",".","6"],
               [".",".",".","2","7","5","9",".","."]]
    result = solveSudoku(myBoard)
    print(result)


"""
APPROACH
- Create 9 sub-boxes, one for each 3x3 square
-- Sub-box is formed by identifying each of the center squares of the boxes and adding
-- 8 surrounding cells

- Keep track of valid candidates for each row, column, and sub-box

- Iterate through the board and when an empty cell is reached attempt to eliminate 
- candidates until only 1 option remains
-- For each candidate in the "square" check if it is a valid candidate in row and col
-- if not, eliminate it and move to the next candidate. If only 1 candidate remains, then
-- it must be the answer


- If no more squares can be filled, then a guess must be made.
-- Will possibly need to use recursion to backtrack in the event the guess is incorrect.
-- Find the candidate with the fewest available options and chose one of those to use as 
-- the guess
"""