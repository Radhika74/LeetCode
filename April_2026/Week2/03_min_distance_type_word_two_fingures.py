class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        A = ord('A')
        index = [ord(c) - A for c in word]
        dp = [float('inf')] * 27
        dp[26] = 0 

        prev = index[0]

        for i in range(1, len(index)):
            cur = index[i]
            new_dp = [float('inf')] * 27

            for free in range(27):
                if dp[free] == float('inf'):
                    continue
                new_dp[free] = min(new_dp[free], dp[free] + dist(prev, cur))
                new_dp[prev] = min(new_dp[prev], dp[free] + dist(free, cur))

            dp = new_dp
            prev = cur

        return min(dp)
