class Solution:
    def longestSubarray(self, nums):
        i = 0
        j = 0
        n = len(nums)
        maxi = 0
        count = 0

        while j < n:
            if nums[j] == 0:
                count += 1

            while count > 1:
                if nums[i] == 0:
                    count -= 1
                i += 1

            maxi = max(maxi, j - i)
            j += 1

        return maxi