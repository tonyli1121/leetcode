# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create list to store data
        result = []

        def traverse(root):
            # base condition
            if root is None:
                return None
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)

        traverse(root)
    
        return result
