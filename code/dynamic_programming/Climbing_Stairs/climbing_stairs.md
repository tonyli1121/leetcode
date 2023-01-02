![image](https://user-images.githubusercontent.com/53313027/210187898-d423e5fa-87e6-4992-9292-c399765c1de3.png)

## Approach 1:

Using recursion and fibonacci number sequence:
  
  ![image](https://user-images.githubusercontent.com/53313027/210187929-14073aab-1e95-4683-ba1d-d7b6ca0d6574.png)
  
  we could easily see that climb(x) = climb(x-1) + climb(x-2)
  
``` python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
```

but only using recursion will give us a TimeLimitOut Exception, because the time complexity is：*Exponential*, as every function calls two other functions

![image](https://user-images.githubusercontent.com/53313027/210188038-61919719-2c05-4047-89b1-731b3a0e12b3.png)


## Approach 2:

Apply memoization and dynamic programming. O(N) time and O(N) space

``` python3
class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,2]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n-1]
```

## Approach 3:

To further optimize on space complexity, we could use loops only:

``` python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(2,n):
            a, b = b, a+b
        return b
```
