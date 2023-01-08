![image](https://user-images.githubusercontent.com/53313027/211176615-ebdedf57-9f53-422a-ab5f-6e7682004e90.png)

## Approach:

We need to realize that we have to generate the entire triangle and therefore has to be at least O(n^2) (1 + 2 + 3 + ... elements)

Hence, simply generate row by row would work and in fact this beats 97+% in time

``` python 3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        last_row = res[0] #
        for i in range(2,numRows+1):
            # iterate through rows
            curr_row = [] # generate curr row
            for j in range(0, i):
                # iterate through curr row, append elements with last row addition
                if j == 0 or j == i-1:
                    curr_row.append(1) # start/end element
                    continue
                curr_row.append(last_row[j-1] + last_row[j])
            res.append(curr_row)
            last_row = curr_row
        return res
```

![image](https://user-images.githubusercontent.com/53313027/211176664-f0322d12-1911-45ed-a7d0-f9663976d6e7.png)

## Reflection

However, when working on this problem (and incl. previous problems), I realized that although I'm passing them with a optimal time, I was running and modifying the code constantly.

I have to keep in mind that in my future practices, I MUST try to ``` pass the tests within as few attempts as possible ```
