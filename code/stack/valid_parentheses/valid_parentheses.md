# Valid Parentheses

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/168444919-22fcd8bf-403c-4122-b7c3-3720ebf5ea79.png)

## Solution:

Use stack's LIFO property to keep track on the brackets

``` python
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        par_dict = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                # if empty but met ),},] return false
                # if LIFO popped is not matching parantheses, return false
                if not stack or par_dict[stack.pop(-1)] != i:
                    return False
        # return true if every brackte is closed
        return not stack
```

![image](https://user-images.githubusercontent.com/53313027/168444951-c0cc0bac-1ffa-4f78-91c5-82cd019bc194.png)




