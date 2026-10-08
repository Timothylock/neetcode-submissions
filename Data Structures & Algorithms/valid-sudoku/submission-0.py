class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = {}
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen[num] = True
        
        for i in range(9):
            seen = {}
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in seen:
                    return False
                seen[row[i]] = True

        for i in range(3):
            for j in range(3):
                seen = {}
                for row in range(3):
                    for col in range(3):
                        if board[i * 3 + row][j * 3 + col] == ".":
                            continue
                        if board[i * 3 + row][j * 3 + col] in seen:
                            return False
                        seen[board[i * 3 + row][j * 3 + col]] = True

        return True

        