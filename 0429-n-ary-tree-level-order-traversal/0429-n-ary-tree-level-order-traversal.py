"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        
        ans = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.popleft()
                temp.append(node.val)
                
                for child in node.children:
                    queue.append(child)
            
            ans.append(temp)
        
        return ans