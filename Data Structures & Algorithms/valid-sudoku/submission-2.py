class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = [{} for _ in range(9)]
        seenCol = [{} for _ in range(9)]
        seenGrid = [{} for _ in range(9)]

        for y in range(9):
            for x in range(9):
                num = board[y][x]
                if num == ".":
                    continue 

                if num in seenRow[y]:
                    return False
                if num in seenCol[x]:
                    return False
                
                gridPos = (x // 3) + (y // 3) * 3
                if num in seenGrid[gridPos]:
                    return False
                
                seenRow[y][num] = 1
                seenCol[x][num] = 1
                seenGrid[gridPos][num] = 1


        return True

        