"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        global ans
        ans = []
        
        def Postorder_Traversal(root):
            global ans
            if root:
                for neighbor in root.children:
                    Postorder_Traversal(neighbor)
                ans.append(root.val)
        
        Postorder_Traversal(root)
        return ans