# Plus One

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/210029277-6effc017-5ddb-48e4-af3c-5369c899dbf9.png)

## Approach 1:

Brute force

``` python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # brute force
        old = '0'
        for i in digits:
            old += str(i)
        new = int(old) + 1
        result = []
        for i in str(new):
            result.append(int(i))
        return result
```

The space complexity is O(n) and the time complexity is O(n)

Worked well.


## Approach 2:

Using one line but still brute force (using [map](https://www.w3schools.com/python/ref_func_map.asp) function)

``` python
return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]
```




