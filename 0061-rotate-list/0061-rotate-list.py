# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head
        
        length = 1
        temp = head
        
        while temp.next:
            length += 1
            temp = temp.next
            
        k = k % length
        if k == 0:
            return head
        
        fast = head
        slow = head
        
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        newHead = slow.next
        slow.next = None
        fast.next = head
        
        return newHead