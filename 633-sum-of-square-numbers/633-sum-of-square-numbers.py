class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hi = int(math.sqrt(c))
        lo = 0
        while lo * lo + hi * hi != c:
            if lo >= hi:
                return 0
            if lo * lo + hi * hi > c:
                hi -= 1
            if lo * lo + hi * hi < c:
                lo += 1
        return 1