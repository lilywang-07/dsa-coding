class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                sq = (i // 3, j // 3)
                if num in rows[i] or num in cols[j] or num in squares[sq]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                squares[sq].add(num)
        return True
