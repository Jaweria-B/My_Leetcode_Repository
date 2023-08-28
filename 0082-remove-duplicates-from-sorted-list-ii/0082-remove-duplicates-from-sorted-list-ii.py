# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            next_node = current.next
            
            while next_node and next_node.val == current.val:
                next_node = next_node.next
                
                
            if current.next != next_node:
                prev.next = next_node
            else:
                prev = current
            
            current = next_node
            
        return dummy.next