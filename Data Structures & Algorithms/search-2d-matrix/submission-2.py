class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom:
            midRow = (top + bottom) // 2

            if target >= matrix[midRow][0] and target <= matrix[midRow][-1]:
                while left <= right:
                    midCol = (left + right) // 2

                    if matrix[midRow][midCol] > target:
                        right = midCol - 1
                    elif matrix[midRow][midCol] < target:
                        left = midCol + 1
                    else:
                        return True
                return False
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
        
        return False