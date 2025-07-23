class Solution:
    def calc(self, tmp: str, x: int, y: int) -> int:
        res = 0

        if x >= y:
            b = 0
            a = 0
            for ch in tmp:
                if ch == 'b':
                    if a > 0:
                        a -= 1
                        res += x
                    else:
                        b += 1
                else:
                    a += 1
            res += min(a, b) * y
        else:
            b = 0
            a = 0
            for ch in tmp:
                if ch == 'a':
                    if b > 0:
                        b -= 1
                        res += y
                    else:
                        a += 1
                else:
                    b += 1
            res += min(a, b) * x

        return res
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        tmp = ""

        for ch in s:
            if ch == 'a' or ch == 'b':
                tmp += ch
            else:
                points += self.calc(tmp, x, y)
                tmp = ""

        if tmp:
            points += self.calc(tmp, x, y)

        return points
        