class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        subgrids = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    entry = int(board[i][j])
                    if entry in rows[i] or entry in cols[j] or entry in subgrids[(j // 3, i // 3)]:
                        return False
                    else:
                        rows[i].append(int(board[i][j]))
                        cols[j].append(int(board[i][j]))
                        subgrids[(j // 3, i // 3)].append(int(board[i][j]))
        
        return True