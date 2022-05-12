# Palindrome Number

**Difficulty** :star:

## Question Description

![image](https://user-images.githubusercontent.com/53313027/167973518-d5acb59f-e0ef-4025-92b9-4d7d55a9881b.png)

## Approach #1

Initially I started with the brute force algorithm, which may take up to **O(N) time complexity**
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
```

Although it passed by beating 27.5% users, it doesn't seem to be a good algorithm
![image](https://user-images.githubusercontent.com/53313027/167973738-03b78bee-c943-4733-908d-9647ef910a0b.png)

## Approach #2

To improve, I considered to use heap to keep track of the elements, which seem to be a better aproach.

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        heap = []
        length = len(tmp)
        for i in range(0, length):
            # construct heap
            if i < len(tmp)//2:            
                heap.append(tmp[i])
            
            # verify second half of str to see if matches heap
            if (length % 2):
                # odd length
                if i > length//2:
                    if heap.pop(-1) != tmp[i]:
                        return False
            else:
                # even length
                if i >= length//2:
                    if heap.pop(-1) != tmp[i]:
                        return False
        return True
```

However, this seem to be a even worse approach, I'm assuming it's caused by using lots for loops, where in previous approach we were using system built-in slicing.

![image](https://user-images.githubusercontent.com/53313027/167974860-31558c0d-da59-4f5f-9e26-05ee23acab08.png)


## Optimal solution:

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
                
        reversed_num = 0
        while reversed_num < x:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return (reversed_num == x or reversed_num // 10 == x)
```

The idea is to use pure math to solve, we keep concatenate the last digits of x to *reversed_num* so that reversed_num acts as a reversion of it, we then compare them
once they have same digits (or if reversed_num have more digits for len(x) is odd).

By checking reversed_num == x or reversed_num // 10 == x we are able to check whether it is a palindrome

If x is equal to reversed number then it is a palindrome

If x has odd number of digits, dicard the middle digit before comparing with x

Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231

So, reversedNum/10 = 23, which is equal to x


