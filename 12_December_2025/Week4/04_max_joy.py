class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            current_joy = happiness[i] - i
            if current_joy <=0:
                break
            total += current_joy
        return total