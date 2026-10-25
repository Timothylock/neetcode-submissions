class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Just a normal binary search, but we will treat it as one big row, and have a helper to help it find where it should be
        rowLength = len(matrix[0])

        l, r = 0, rowLength * len(matrix) - 1
        while l <= r:
            middle = (l+r) // 2
            row = middle // rowLength
            col = middle % rowLength


            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False