# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        temp = head
        fastemp = head
        while fastemp and fastemp.next:
            temp = temp.next
            fastemp = fastemp.next.next
            if temp == fastemp:
                return True
                
        return False