class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        size = len(set(nums))
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # find non-duplicate, set it to corresponding index
                nums[length] = nums[i]
                length+=1
            if (length == size):
                # no need to run following iterations because we achieved size
                break
        return length
