class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        n = len(board)

        #row counter
        for i in range(n):
            c1 = defaultdict(int)
            for j in range(n):
                #row-counter
                if board[i][j].isdigit():
                    c1[board[i][j]] += 1
            
            dups_rows = any(v > 1 for v in c1.values())
            if dups_rows:
                return False

        #column counter
        
        for i in range(n):
            c1 = defaultdict(int)
            for j in range(n):
                if board[j][i].isdigit():
                    c1[board[j][i]] += 1
            dups_cols = any(v > 1 for v in c1.values())
            if dups_cols:
                return False

            
        #block counter
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
                    


