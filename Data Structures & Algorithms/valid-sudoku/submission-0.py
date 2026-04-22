class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col //3)]): 
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[row // 3, col // 3].add(board[row][col])
        return True
"""
Goal: make sure every column, row, and 3x3 square are all valid

hashset to keep track of duplicate entries
keep 3: rows, cols, 3x3 squares

create a set for rows
create a set for cols
create a set for 3x3 squares

iterate through the cols
    check to see if the value at this col position is in the cols set
    iterate through the rows:
        check to see if the value at this poition is in the rows set

        check to see if the value in the square is already in the squares set

return true if valid sudoku
"""
        