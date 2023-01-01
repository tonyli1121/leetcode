class Solution:
    def isRoundedRoot(self, x: int, target: int) -> bool:
        ''' Returns True if x is the rounded root of target '''
        if (x*x <= target) and ((x+1)*(x+1) > target):
            return True
        return False

    def mySqrt(self, x: int) -> int:
        # idea: use BINARY SEARCH to partition from half

        # special case of 0 and 1, can't partition by half
        if x==0 or x==1:
            return x
        lo, hi = 0, x
        found = False
        while (not found):
            n = lo + (hi - lo)//2
            if self.isRoundedRoot(n, x):
                found = True
            elif n * n < x:
                # search right half
                lo = n+1
            else:
                # search left half
                hi = n-1
        return n   
