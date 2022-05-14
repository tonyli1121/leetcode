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
