# Merge Two Sorted Lists

**Difficulty** :star::star:

Keep in mind that DFS is preferred in interview than BFS

**Theory -**

For *DFS*, *depth of recurrence(extra space required) is equal to height of tree* and for balanced tree it will be log(n) so Space complexity is **O(log n)**.
For *BFS*, *lowest layer of tree will have n/2 nodes* and hence queue will grow to n/2 size while processing lowest layer of tree. Space complexity is **O(n)**.

**Practically -**

Thread stack size is much smaller than heap size(like -2MB vs 20GB). So DFS will throw StackOverFlow error for unbalanced tree way before BFS will throw OutOfMemoryError for a large tree.


## Question Description

![image](https://user-images.githubusercontent.com/53313027/169117201-f60b7bf1-5dc9-4a57-8b68-4159fe548d2c.png)

## Approach #1

This can easily solved using DFS recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def getTargetCopy(self, node1: TreeNode, node2: TreeNode, target: TreeNode) -> TreeNode:        
        if not node1 or target == node1:  # if node1 is null, node2 will also be null
            return node2
        
        return self.getTargetCopy(node1.left, node2.left, target) or self.getTargetCopy(node1.right, node2.right, target) 
```

This is quite slow in time as it traverse all nodes, however, there's no other way than check every single node as it is unsorted. Otherwise we could consider sort it first but it would take O(NlogN) time first for sorting and another O(logN) to search
![image](https://user-images.githubusercontent.com/53313027/169117732-017b882c-977f-4d67-b406-ae97149010f6.png)





