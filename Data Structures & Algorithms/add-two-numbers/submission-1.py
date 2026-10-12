# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify handling the head of the new list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop as long as there are nodes left in either list, or a carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create the new node with the single digit value
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
