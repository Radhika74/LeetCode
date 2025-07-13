class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 +7
        if not word:
            return 0
        
        grp=[]
        count=1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count +=1
            else:
                grp.append(count)
                count=1
        grp.append(count)

        total=1
        for j in grp:
            total=(total*j)%MOD
        
        if k<=len(grp):
            return total
        
        dp=[0]*k
        dp[0]=1

        for j in grp:
            new_dp=[0]*k
            sum_=0
            for s in range(k):
                if s > 0:
                    sum_ = (sum_ + dp[s-1]) % MOD
                if s > j:
                    sum_ = (sum_ - dp[s - j - 1] + MOD) % MOD
                new_dp[s] = sum_
            dp = new_dp

    
        invalid = sum(dp[len(grp):]) % MOD
        return (total - invalid + MOD) % MOD