class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        k2 = k//2
        profit =[strategy[i] * prices[i] for i in range(n)]
        prefixP = [0] * (n+1)
        prefixA = [0] * (n+1)
        for i in range(n):
            prefixP[i + 1] = prefixP[i] + prices[i]
            prefixA[i + 1] = prefixA[i] + profit[i]

        og_profit = prefixA[n]
        max_delta = 0
        for l in range(n - k + 1):
            delta = (prefixP[l + k] - prefixP[l + k2]) - (prefixA[l + k] - prefixA[l])
            if delta > max_delta:
                max_delta = delta
        return og_profit + max_delta