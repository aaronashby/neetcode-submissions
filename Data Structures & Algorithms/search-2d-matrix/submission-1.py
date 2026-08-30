class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowToSearch = -1
        rowLeft, rowRight = 0, len(matrix) - 1

        while rowLeft <= rowRight:
            rowMid = (rowLeft + rowRight) // 2

            if target > matrix[rowMid][-1]:
                rowLeft = rowMid + 1
            elif target < matrix[rowMid][0]:
                rowRight = rowMid - 1
            else:
                rowToSearch = rowMid
                break
        
        if rowToSearch == -1:
            return False
        
        row = matrix[rowToSearch]
        colLeft, colRight = 0, len(row) - 1

        while colLeft <= colRight:
            colMid = (colLeft + colRight) // 2

            if row[colMid] < target:
                colLeft = colMid + 1
            elif row[colMid] > target:
                colRight = colMid - 1
            else:
                return True
        
        return False