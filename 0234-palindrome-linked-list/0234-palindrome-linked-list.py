# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast != None and fast.next == None:
            slow = slow.next

        prev = None
        temp = None

        while slow != None and slow.next != None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if slow != None:
            slow.next = prev

        fast = head

        while slow and fast:

            if slow.val != fast.val:
                return False

            slow = slow.next 
            fast = fast.next

        return True