class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        power = []
        for i in range(32):
            if (n >> i) & 1:
                power.append(1 << i)
        result = []
        for start, end in queries:
            product = 1
            for i in range(start, end + 1):
                product = (product * power[i]) % MOD
            result.append(product)
            
        return result