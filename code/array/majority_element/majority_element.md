![image](https://user-images.githubusercontent.com/53313027/212573769-e890fe02-4384-4b0a-a30a-c6c95aa1922f.png)

## Approach 1:

We could solve by brute force, that is, counting the time each element appear in a dictionary and return the one appeared the most.

This would have a time complexity of O(N) and space complexity of O(N)

## Approach 2:

Since it's given that the majority element would appear at least n/2 times, then if we sort the list and take the middle element, we always get the majority element.

It will have a time complexity of O(NlogN) and space complexity of O(1)

``` python 3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
```

![image](https://user-images.githubusercontent.com/53313027/212573859-db0dcba5-00b5-4072-b8ac-a9335e4f57e5.png)


## Approach 3:

To count the majority element, we could consider let them eliminate, which is also called [Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm#:~:text=The%20Boyer%E2%80%93Moore%20majority%20vote,example%20of%20a%20streaming%20algorithm.)

The idea is that everytime an element occurs, we let it eliminate the count of another different element, and the one left would always have appeared at least n/2 times, making it therefore the majority element

This has a time complexity of O(N) and space complexity of O(1).

``` python 3
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
```

![image](https://user-images.githubusercontent.com/53313027/212573946-c4f76ab9-e748-47ee-b032-d34de86e21a0.png)

