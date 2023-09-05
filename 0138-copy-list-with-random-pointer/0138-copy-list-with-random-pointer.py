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
        
        curr = head
        dic = { None: None}
        
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = dic[curr]
            copy.next = dic[curr.next]
            copy.random = dic[curr.random]
            curr = curr.next
        
        return dic[head]