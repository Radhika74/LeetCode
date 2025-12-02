class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, -10**18, -10**18]   # use big negative int instead of -inf
        
        for x in nums:
            temp = dp[:]             # copy current states
            for r in range(3):
                ns = temp[r] + x     # new sum
                dp[ns % 3] = max(dp[ns % 3], ns)
        
        return dp[0]
