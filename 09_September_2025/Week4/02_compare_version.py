class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        n, m = len(version1), len(version2)

        while i < n or j < m:
            num1, num2 = 0, 0

            # parse version1 segment
            while i < n and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1

            # parse version2 segment
            while j < m and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1

            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

            # skip the dot
            i += 1
            j += 1

        return 0