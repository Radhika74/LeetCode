class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maximum = -1.0
        res =0

        for l,b in dimensions:
            d=math.sqrt(l*l+b*b)
            if d>maximum:
                maximum = d
                res = l*b
            elif d == maximum:
                res =max(res, l*b)
        return res