# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node == None:
                return set()
            left = dfs(node.left)
            right = dfs(node.right)
            if isinstance(left, TreeNode):
                return left
            elif isinstance(right, TreeNode):
                return right
            result = (left | right)
            result.add(node)
            if q in result and p in result:
                return node
            return result
        return dfs(root)