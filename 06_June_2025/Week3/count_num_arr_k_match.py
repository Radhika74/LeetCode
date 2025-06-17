class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = int(1e9) + 7
        a = math.comb(n-1, k) % MOD 
        b = m 
        c = (m-1)**(n-1-k) % MOD
        return (((a * b) % MOD)*c)%MOD