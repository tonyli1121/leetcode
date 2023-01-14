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
