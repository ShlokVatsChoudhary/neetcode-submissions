# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        t1 = l1
        multiplier = 1
        while t1:
            n1 = t1.val *multiplier + n1
            t1 = t1.next
            multiplier *= 10

        n2 = 0
        t2 = l2
        multiplier = 1
        while t2:
            n2 = t2.val *multiplier + n2
            t2 = t2.next
            multiplier *= 10

        n3 = n1+n2

        head = ListNode(n3%10)
        n3 //= 10
        t = head
        while n3:
            t.next = ListNode(n3%10)
            n3 //= 10
            t = t.next

        return head