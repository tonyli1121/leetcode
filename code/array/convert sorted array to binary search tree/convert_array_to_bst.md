![image](https://user-images.githubusercontent.com/53313027/211175992-44746fa1-7ca6-4ba0-88ab-cfb070043767.png)

## Approach:

Note that there are two major properties of the given input:

1. The array is sorted
2. The result should be balanced (in height)

This gives us a hint that ```nums[len(nums)//2]``` would always be the ```root of the subtree generated with nums```

Hence, by applying techniques from divide and conquer, we could divide the problem into subtrees and recursively solve it.

``` python 3
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
```

Although recursion tends to use more space than solving with memoization, it still has a time complexity of O(NlogN) and beats 90+% in time and 80+% in space.

![image](https://user-images.githubusercontent.com/53313027/211176050-9db4fe3f-aba3-4761-acda-cb6d141fc824.png)
