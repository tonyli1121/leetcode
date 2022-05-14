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
