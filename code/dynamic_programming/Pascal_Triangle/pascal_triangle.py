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
