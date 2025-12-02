class Solution:
    def totalMoney(self, n: int) -> int:
        mon=0
        count=0
        total=0
        for i in range(1,n+1):
            if count==7:
                mon= i//7+1
                count=0
            else:
                mon+=1
            total+=mon
            count+=1
        return total