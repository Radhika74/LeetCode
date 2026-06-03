class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for val in nums:
            for char in str(val):
                ans.append(int(char))
        return ans
