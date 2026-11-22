# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 == None or root2 == None:
                return False
            elif root1.val != root2.val:
                return False
            left = equal(root1.left, root2.left)
            right = equal(root1.right, root2.right)
            return (left and right)

        def recurse(node):
            if node == None:
                return False
            elif node.val == subRoot.val and equal(node, subRoot):
                return True
            left = recurse(node.left)
            right = recurse(node.right)
            return left or right

        if root == None and subRoot == None:
            return True
        elif root == None or subRoot == None:
            return False
        return recurse(root)
        