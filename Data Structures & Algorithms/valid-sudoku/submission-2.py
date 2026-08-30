class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        subBoxes = defaultdict(list)

        for rowIdx in range(9):
            for colIdx in range(9):
                if board[rowIdx][colIdx] == ".":
                    continue
                
                num = int(board[rowIdx][colIdx])

                if num in rows[rowIdx] or num in cols[colIdx] or num in subBoxes[(rowIdx // 3, colIdx // 3)]:
                    return False
                
                rows[rowIdx].append(num)
                cols[colIdx].append(num)
                subBoxes[(rowIdx // 3, colIdx // 3)].append(num)
        
        return True