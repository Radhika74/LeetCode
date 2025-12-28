class Solution:
    def countNegatives(self, grid):
        count = 0

        for row in grid:
            first_negative = len(row)
            for i, value in enumerate(row):
                if value < 0:
                    first_negative = i
                    break
            count += len(row) - first_negative

        return count