# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        global front
        front = head
        
        def recursive(curr):
            global front 
            
            if curr != None:
                
                if not recursive(curr.next):
                    return False
                
                if curr.val != front.val:
                    return False
                
                front = front.next
                
            return True
        
        return recursive(head)