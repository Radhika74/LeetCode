class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        l = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[l] > k:
                ans += 1
                l = i
        return ans