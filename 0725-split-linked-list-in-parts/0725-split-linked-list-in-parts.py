# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        
        width, remainder = divmod(N, k)
        
        ans = []
        cur = head
        for i in range(k):
            head = write = ListNode(None)
            for j in range( width + ( i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans        