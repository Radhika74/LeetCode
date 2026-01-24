class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j:
            pair_sum = nums[i] + nums[j]
            res = max(res, pair_sum)
            i += 1
            j -= 1
        return res