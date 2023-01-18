![image](https://user-images.githubusercontent.com/53313027/213247293-0cbb3977-20f1-42fe-a68d-aa02292ddb0f.png)


## Approach:

We have to brute force check all posibilities to avoid missing until we see a repeated number (as specified in the question, loop endlessly).

``` python 3
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n):
        res = 0
        while n:
            n, d = divmod(n, 10)
            res += d * d
        return res
```
