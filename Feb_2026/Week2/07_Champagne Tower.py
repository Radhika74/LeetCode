class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]
        for i in range(1, query_row + 1):
            curr = [0] * (i + 1)
            for j in range(i):
                extra = prev[j] - 1
                if extra > 0:
                    curr[j] += extra * 0.5
                    curr[j + 1] += extra * 0.5
            prev = curr
        return min(1, prev[query_glass])
