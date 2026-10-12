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
        if not head:
            return None
        
        # Dictionary to map original nodes to their corresponding copied nodes
        old_to_new = {}
        
        # Step 1: Create all new nodes and map old -> new
        temp1 = head
        while temp1:
            old_to_new[temp1] = Node(temp1.val)
            temp1 = temp1.next
            
        # Step 2: Connect the next and random pointers for the new nodes
        temp1 = head
        while temp1:
            new_node = old_to_new[temp1]
            
            # Connect next pointer (if it exists)
            new_node.next = old_to_new[temp1.next] if temp1.next else None
            
            # Connect random pointer (if it exists)
            new_node.random = old_to_new[temp1.random] if temp1.random else None
            
            temp1 = temp1.next
            
        return old_to_new[head]

