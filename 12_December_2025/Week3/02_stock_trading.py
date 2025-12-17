class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        dp = [[[0] * (budget + 1) for _ in range(2)] for _ in range(n)]
        NEG = -10**15

        def merge(a, b):
            for i in range(budget, -1, -1):
                for j in range(i + 1):
                    a[i] = max(a[i], a[i - j] + b[j])
            return a

        def dfs(u):
            # merge children once
            child0 = [0] * (budget + 1)
            child1 = [0] * (budget + 1)

            for v in tree[u]:
                dfs(v)
                child0 = merge(child0, dp[v][0][:])
                child1 = merge(child1, dp[v][1][:])

            # parent NOT bought
            dp0 = child0[:]
            cost = present[u]
            profit = future[u] - cost
            for b in range(budget, cost - 1, -1):
                dp0[b] = max(dp0[b], child1[b - cost] + profit)

            # parent bought
            dp1 = child0[:]  # skip still uses dp[v][0]
            cost //= 2
            profit = future[u] - cost
            for b in range(budget, cost - 1, -1):
                dp1[b] = max(dp1[b], child1[b - cost] + profit)

            dp[u][0] = dp0
            dp[u][1] = dp1

        dfs(0)
        return max(dp[0][0])