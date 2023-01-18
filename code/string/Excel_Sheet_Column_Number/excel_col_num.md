![image](https://user-images.githubusercontent.com/53313027/213060238-ea5e0cac-9519-4f82-81ab-537ad184ba95.png)


## Approach:

The idea is to traverse the col string, and adds up the corresponding numbers. We need to increment the exponent by 1 (i.e., A = 1, AA = 26^1 + 1, AAA = 26^2 + ...)

``` python 3
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans
```

It is an O(N) algo.

![image](https://user-images.githubusercontent.com/53313027/213060463-ed0e9474-22e9-4c9e-a173-957b9b6ba20a.png)
