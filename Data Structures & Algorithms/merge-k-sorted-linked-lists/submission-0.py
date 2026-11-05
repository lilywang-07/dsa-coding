# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide(lists, l, r):
            if len(lists) == 0:
                return
            elif l > r:
                return
            elif l == r:
                return lists[l]
            mid = (l+r) // 2
            left = divide(lists, l, mid)
            right = divide(lists, mid+1, r)
            head = ListNode()
            tail = head
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return head.next
        return divide(lists, 0, len(lists) - 1)