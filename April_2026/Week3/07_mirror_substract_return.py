class Solution:
    def revnum(self, n: int) -> int:
        if n//10 ==0:
            return n
        return int(str(n)[::-1])
    def mirrorDistance(self, n: int)->int:
        return abs(n-self.revnum(n))
