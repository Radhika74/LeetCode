import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                c_square = i * i + j * j 
                c = math.isqrt(c_square)
                if c * c == c_square and c <= n:
                    count += 1
        return count
