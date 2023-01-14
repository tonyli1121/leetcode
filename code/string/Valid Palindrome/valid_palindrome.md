![image](https://user-images.githubusercontent.com/53313027/212443013-2770ce82-7713-4442-87be-88bfa3e20a03.png)


## Approach 1:

use an extra string to store all the chars that are alpha/numeric, then check if it matches itself in the reversed order

``` python 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # method 1
        # convert s in to a string without non-alphanumeric
        new_string = ""
        for i in s.replace(' ', ''):
            # traverse s omitting spaces
            if i.isalnum():
                new_string += i
        
        return new_string.lower()[::] == new_string.lower()[::-1]
```
![image](https://user-images.githubusercontent.com/53313027/212443124-299c9c80-13ca-41ae-bcfa-be66481a5e4f.png)



## Approach 2:

We could also consider using less space, by just using two pointers instead of storing an extra string.

``` python 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # method 2, two pointers
        # init two pointers to be the start/end of string
        l, r = 0, len(s) - 1

        while l < r:
            # move l and r one step closer to each other
            # (ignoring the non-alphanumeric chars)
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            # every single iter, the left side and right
            # side of the string needs to match for it to
            # be a palindrome
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
```

![image](https://user-images.githubusercontent.com/53313027/212443133-e366d145-7249-43d8-b689-fbba263b5544.png)


## Conclusion

Both of the algorithms are O(N) and uses O(1) space, hence we don't see much difference in the time/space complexity between two methods.

However, the two pointer is always useful to keep in mind as it usually allows us to save some space (might be a good technique in interview.
