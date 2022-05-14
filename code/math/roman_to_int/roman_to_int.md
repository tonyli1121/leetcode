# Roman To Integer

**Difficulty** :star:

## Question Description

![image](https://user-images.githubusercontent.com/53313027/168444404-1e5bef87-86b4-4d6b-b5e0-b23f0e591e97.png)

## Solution

This question is very straight forward. We can just use a hash table (dictionary) to store all the corresponding values for each roman letter, then add them up for every iteration. We just need to notice that if a roman letter with small value (i.e., "I" = 1) appears before some larger ones (i.e., "V" = 5), we need to minus it so it constructs a decremented value (i.e. "IV" = -1 + 5 = 4)

``` python
class Solution:
    def romanToInt(self, s: str) -> int:
        lookup_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        for i in range(len(s)):
            # for case IV, IX, XL, XC, CD, CM we need to subtract the previous char
            if i + 1 < len(s) and lookup_dict[s[i]] < lookup_dict[s[i+1]]:
                res -= lookup_dict[s[i]]
            else:
                res += lookup_dict[s[i]]
        return res
```


