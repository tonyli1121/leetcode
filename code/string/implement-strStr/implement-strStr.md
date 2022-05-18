# Implement strStr

**Difficulty** :star:


## Question Description

![image](https://user-images.githubusercontent.com/53313027/169114239-9cde4b8c-3125-4ecd-a230-e96aef9afd3c.png)

## Approach #1

Initially I started with calling python's builtin function string.index()
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)
```

As a built-in function, its' space complexity is low as expected, however there can be more improvement on time complexity
![image](https://user-images.githubusercontent.com/53313027/169114464-2c0c0d99-75b3-4a5b-be34-a3c22aa6a61f.png)

## Approach #2

To improve, I considered to manually implement the index function, considering that near the end of *haystack* we don't need to concern about the substring (i.e., hello, substring = 'loo', we only need to check until index 2, becasue once we reach index 3, the string 'lo' has smaller length than 'loo' and therefore can never be the case)

``` python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_needle = len(needle)
        len_haystack = len(haystack)
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
```

It seem to be an improvement on time and the space complexity maintained the same (still O(1))

![image](https://user-images.githubusercontent.com/53313027/169116057-87d9915c-f613-46be-a892-1014c316c091.png)




