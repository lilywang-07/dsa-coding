# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = 0
        head = ListNode(None)
        curr = head
        def add(n1, n2):
            nonlocal curr
            nonlocal carry
            curr.next = ListNode(None)
            curr = curr.next
            add = n1 + n2 + carry
            term = add % 10
            if add >= 10:
                carry = 1
            else:
                carry = 0
            curr.val = term

        while l1 and l2:
            add(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            add(l1.val, 0)
            l1 = l1.next
        while l2:
            add(l2.val, 0)
            l2 = l2.next
        if carry == 1:
            curr.next = ListNode(None)
            curr = curr.next
            curr.val = 1
        return head.next