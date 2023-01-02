class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(2,n):
            a, b = b, a+b
        return b
