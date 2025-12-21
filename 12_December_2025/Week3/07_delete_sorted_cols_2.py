class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res =0
        rows = len(strs)
        cols = len(strs[0])
        sorted_pairs = [False] * (rows - 1)

        for c in range(cols):
            bad = False
            for r in range(rows-1):
                if not sorted_pairs[r] and strs[r][c]>strs[r+1][c]:
                    bad = True
                    break
            if bad:
                res +=1
                continue
            for i in range(rows-1):
                if not sorted_pairs[i] and strs[i][c] < strs[i + 1][c]:
                    sorted_pairs[i] = True
            if all(sorted_pairs):
                break
        return res
