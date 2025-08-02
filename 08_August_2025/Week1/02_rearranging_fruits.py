class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter()
        minimum = float('inf')
        for x in basket1:
            count[x] +=1
            minimum = min(minimum, x)

        for x in basket2:
            count[x]-=1
            minimum =min(minimum, x)
        
        total =0

        for v in count.values():
            if v%2 !=0:
                return -1
            total+=abs(v)
        im=[]
        for num, v in count.items():
            im.extend([num]*(abs(v)//2))
        
        im.sort()
        half =len(im)//2
        double_min =2*minimum
        ans =sum(min(im[i], double_min) for i in range(half))
        return ans