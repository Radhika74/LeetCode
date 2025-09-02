from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                # must satisfy x1 <= x2 and y1 >= y2
                if not (x1 <= x2 and y1 >= y2):
                    continue

                blocked = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    x, y = points[k]

                    # check if point k is inside rectangle formed by (x1,y1) and (x2,y2)
                    if x1 <= x <= x2 and y2 <= y <= y1:
                        blocked = True
                        break

                if not blocked:
                    count += 1

        return count
