# Maximum Subarray

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/169418997-17574af7-6c23-4118-841f-8c62c36bbefe.png)

## Approach 1:

Brute force

``` python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        size = len(nums)
        for i in range(0, size):
            cur_sum = 0
            for j in range(i, size):
                cur_sum += nums[j]
                max_sum = max(cur_sum, max_sum)
                
        return max_sum
```

The space complexity is O(n^2) and the time complexity is O(1)

Did not work and exceeded time limit.

![image](https://user-images.githubusercontent.com/53313027/169419039-426e89fd-a53f-46c2-8851-e3cdcdef1cb2.png)


## Approach 2:

Using *Kadane's Algorithm*

![image](https://user-images.githubusercontent.com/53313027/169419362-325e8313-8ccf-46a3-bbc6-df0ce36f8be3.png)


``` python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        return maxSum
```

![image](https://user-images.githubusercontent.com/53313027/169419555-a3165ecd-33b8-487b-8670-01e825597ad4.png)


The time is O(N)


![image](https://user-images.githubusercontent.com/53313027/169419443-712c585f-15be-45be-80ee-223252d365a6.png)






