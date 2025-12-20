class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res =0
        rows = len(strs)
        cols = len(strs[0])

        for i in range(cols):
            for j in range(rows-1):
                if strs[j][i]>strs[j+1][i]:
                    res+=1
                    break
        return res
