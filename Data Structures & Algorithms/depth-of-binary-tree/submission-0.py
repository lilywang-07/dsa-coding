# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root is None:
                return depth
            depth += 1
            right = dfs(root.right, depth)
            left = dfs(root.left, depth)
            return max(left, right)
        return dfs(root, 0)
