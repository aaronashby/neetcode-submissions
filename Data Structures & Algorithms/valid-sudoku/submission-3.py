class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoxes = defaultdict(set)

        for rowIdx in range(9):
            for colIdx in range(9):
                if board[rowIdx][colIdx] == ".":
                    continue
                
                num = int(board[rowIdx][colIdx])

                if num in rows[rowIdx] or num in cols[colIdx] or num in subBoxes[(rowIdx // 3, colIdx // 3)]:
                    return False
                
                rows[rowIdx].add(num)
                cols[colIdx].add(num)
                subBoxes[(rowIdx // 3, colIdx // 3)].add(num)
        
        return True