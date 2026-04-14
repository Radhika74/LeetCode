class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp=deafultdict(list)
        n=len(nums)
        for i in range(n):
            np[nums[i]].append(i)
        ans = float('inf')
        for indices in mp.values():
            if len(indices)<3:
                continue
            for i in range(len(indices)-2):
                dist=2*(indices[i+2]-indices[i])
                ans=min(ans,dist)
        return -1 if ans == float('inf') else ans
