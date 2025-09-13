class Solution:
    def maxFreqSum(self, s: str) -> int:
        d=Counter(s)
        c, v=0, 0
        for i in s:
            if i in 'aeiou':
                v=max(v, d[i])
            else:
                c=max(c, d[i])
        return c+v