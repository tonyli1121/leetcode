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
