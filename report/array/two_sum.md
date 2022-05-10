# Two Sum

**Difficulty** :star:

---
Initially I started with the brute force algorithm, which may take up to **O(N^2) time complexity**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force traverse all
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

To improve, I considered to apply a sorting first with O(NlogN), then do a BFS on every number with target so that for each iteration it would be O(logN). And will result it to be a **O(NlogN)** algo.

