# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        
        less_Nodes = ListNode(0)
        less_tail = less_Nodes
        
        greater_Nodes = ListNode(0)
        greater_tail = greater_Nodes
        
        while current:
            if current.val < x:
                less_tail.next = ListNode(current.val)
                less_tail = less_tail.next
                
            else:
                greater_tail.next = ListNode(current.val)
                greater_tail = greater_tail.next
                
            current = current.next
        
        less_tail.next = greater_Nodes.next
        
        return less_Nodes.next