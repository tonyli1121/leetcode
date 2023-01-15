class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
      
      
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 1
        for i in nums:
            if result == i:
                count += 1
            else:
                count -= 1
            if count == 0:
                result = i
                count = 1
        return result
