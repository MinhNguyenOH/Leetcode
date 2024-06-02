class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for c in range(len(board)):
            for r in range(len(board[0])):
                if board[r][c] != ".":
                    if (board[r][c] not in cols[c] and board[r][c] not in rows[r] and board[r][c] not in squares[(r//3, c//3)]):
                        cols[c].add(board[r][c])
                        rows[r].add(board[r][c])
                        squares[(r//3, c//3)].add(board[r][c])
                    else:
                        return False
                
        return True