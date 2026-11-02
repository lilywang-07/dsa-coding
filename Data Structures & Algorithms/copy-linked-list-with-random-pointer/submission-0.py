"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        def dfs(curr):
            if curr is None:
                return None
            if curr in old_to_new:
                return old_to_new[curr]
            copy = Node(curr.val)
            old_to_new[curr] = copy
            copy.next = dfs(curr.next)
            copy.random = dfs(curr.random)
            return copy

        return dfs(head)