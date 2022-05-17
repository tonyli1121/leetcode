# Remove Duplicates from Sorted Array

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/168874763-4271828e-1d97-4aa0-9a39-6bcaa2c2ad9f.png)

## Approach 1:

keep iterating the list, once we see a non-duplicate element, set it to corresponding index

``` python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # find non-duplicate, set it to corresponding index
                nums[length] = nums[i]
                length+=1
        return length
```

The space complexity is O(1) and the time complexity is O(n)

## Approach 2:

add another variable size, which helps us determine when to break the loop.

``` python
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
```

The size is still O(1), and time will be faster especially for case such as [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5]



The performance overall is the same, and our best result is defeating 87% in time and 96% in space

![image](https://user-images.githubusercontent.com/53313027/168875368-c79538a0-7ce3-4f07-9350-31bf65a347c2.png)

![image](https://user-images.githubusercontent.com/53313027/168875286-c1c1c4d5-e4b1-4f42-842b-46ff3a00a696.png)





