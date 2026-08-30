class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                # Check row
                for r in range(9):
                    if row != r and board[r][col] == board[row][col]:
                        return False
                
                # Check column
                for c in range(9):
                    if c != col and board[row][c] == board[row][col]:
                        return False
                
                # Check sub-box
                subBoxRow = row // 3
                subBoxCol = col // 3

                for sbRow in range(subBoxRow * 3, (subBoxRow * 3) + 3):
                    for sbCol in range(subBoxCol * 3, (subBoxCol * 3) + 3):
                        if sbRow != row and sbCol != col and board[row][col] == board[sbRow][sbCol]:
                            return False

        return True 
