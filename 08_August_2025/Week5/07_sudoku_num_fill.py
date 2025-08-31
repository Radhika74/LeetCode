class Solution:
    def solveSudoku(self, board):
        # Use sets for quick lookup
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(i=0):
            if i == len(empty):
                return True  # solved all cells

            r, c = empty[i]
            b = (r // 3) * 3 + (c // 3)

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(i + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack()
