class Solution:
    def canFinish(self, T: int, mountainHeight: int, workerTimes: List[int]) -> bool:
        total = 0

        for w in workerTimes:
            x = int((math.sqrt(1 + 8 * T / w) - 1) / 2)

            while w * x * (x + 1) // 2 > T:
                x -= 1
            while w * (x + 1) * (x + 2) // 2 <= T:
                x += 1

            total += x
            if total >= mountainHeight:
                return True

        return total >= mountainHeight

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        low = 0
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.canFinish(mid, mountainHeight, workerTimes):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
