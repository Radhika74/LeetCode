class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        cnt =0
        for i in capacity:
            total -=i
            cnt+=1
            if total<=0:
                return cnt
        return cnt