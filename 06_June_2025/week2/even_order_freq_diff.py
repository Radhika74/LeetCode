class Solution:
    def maxDifference(self, s: str) -> int:
        total_Alpha = [0]*26
        maxi = 0
        mini = len(s)
        for i in s:
            total_Alpha[ord(i) - ord('a')] += 1
        for i in range(26):
            if total_Alpha[i] % 2 != 0:
                maxi = max(maxi, total_Alpha[i])
            if total_Alpha[i] % 2 == 0 and total_Alpha[i] > 0:
                mini = min(mini, total_Alpha[i])
        return maxi - mini