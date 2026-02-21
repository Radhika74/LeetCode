class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p = {2, 3, 5, 7, 11, 13, 17, 19}
        r = 0
        for n in range(left,right+1):
            if bin(n).count("1") in p:
                r += 1
        return r    
