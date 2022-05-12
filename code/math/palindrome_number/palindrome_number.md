# Palindrome Number

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/167973518-d5acb59f-e0ef-4025-92b9-4d7d55a9881b.png)

---
Initially I started with the brute force algorithm, which may take up to **O(N) time complexity**
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
```

Although it passed by beating 27.5% users, it doesn't seem to be a good algorithm
![image](https://user-images.githubusercontent.com/53313027/167973738-03b78bee-c943-4733-908d-9647ef910a0b.png)

---

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


---

## Optimal solution:



