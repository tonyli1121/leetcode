# Two Sum

**Difficulty** :star:

![image](https://user-images.githubusercontent.com/53313027/167694312-9727d717-a70f-44e3-b63e-8457363f0de0.png)

---
Initially I started with the brute force algorithm, which may take up to **O(N^2) time complexity**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force traverse all
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

Although it passed by beating 25% users, it doesn't seem to be a good algorithm
![image](https://user-images.githubusercontent.com/53313027/167694045-08f6e6af-78a2-480e-9efe-1fc25d7bd3d1.png)

---

To improve, I considered to apply a sorting first with O(NlogN), then do a BFS on every number with target so that for each iteration it would be O(logN). And will result it to be a **O(NlogN)** algo.

``` python
class Solution:
    '''
    binary search of a list, return index of key in nums[start:end] as an integer
    '''
    def binary_search(self, nums:List[int], key, start, end) -> int:
        # found key
        if end - start <= 1:
            if key < nums[start]:
                return start-1
            return start
        # otherwise recursively run binary_search
        mid = (start + end) // 2
        if nums[mid] < key:
            return self.binary_search(nums, key, mid, end)
        elif nums[mid] > key:
            return self.binary_search(nums, key, start, mid)
        else:
            return mid
    
    '''
    Modify the given list nums using binary insertion sort, time comlexity O(nlogn)
    '''
    def insertion_sort(self, nums:List[int]) -> None:
        for i in range (1, len(nums)):
            tmp = nums[i]
            pos = self.binary_search(nums, tmp, 0, i) + 1
            for k in range(i, pos, -1):
                nums[k] = nums[k - 1]
            nums[pos] = tmp
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a copy of nums so that we are not messed up with sorted list indices
        nums_copy = []
        for i in nums:
            nums_copy.append(i)
        self.insertion_sort(nums)
        end = len(nums)
        for i in range(0,end):
            res = self.binary_search(nums, target - nums[i], 0, end)
            if (nums[i] + nums[res] == target):
                res_1 = i
                res_2 = res
        # refer back to original list for index
        for i in range(0,end):
            if nums_copy[i] == nums[res_1]:
                res_1 = i
                break
        for i in range(0,end):
            if nums_copy[i] == nums[res_2]:
                if (i == res_1):
                    continue
                res_2 = i
                break
        return [res_1, res_2]
```

![image](https://user-images.githubusercontent.com/53313027/167701099-aeec18c1-5669-4537-80ad-332d55cb528c.png)

Although there is an improvement on the algorithm running time, it is still not optimal. One of the problem I think is that I used some O(n) loop too many times.

---

Optimal solution:

use enumerate to keep track of value - index, store in a dictionary. Then look up the remaining value of current iteration from the dictionary (O(1) look up for dict)

``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
           
            if remaining in seen:
                return [i, seen[remaining]]
            
            seen[value] = i 
            ```


