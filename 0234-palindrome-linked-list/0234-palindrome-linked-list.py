# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        if head == None or head.next == None:
            return head

        r_head = None 
        ptr = head

        while ptr:
            temp = ListNode(ptr.val)
            temp.next = r_head
            r_head = temp
            ptr = ptr.next

        while head and r_head:
            if head.val != r_head.val:
                return False
            head = head.next
            r_head = r_head.next

        return True