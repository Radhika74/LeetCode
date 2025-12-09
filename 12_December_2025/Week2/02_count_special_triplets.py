import math
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        MOD =10**9 +7

        right = Counter(nums)
        left = Counter()
        ans=0
        for i, val in enumerate(nums):
            right[val]-=1
            if right[val]==0:
                del right[val]
            target = val*2
            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD
            left[val] += 1
        return ans
            