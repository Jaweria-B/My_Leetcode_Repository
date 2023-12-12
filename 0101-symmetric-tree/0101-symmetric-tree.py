# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = collections.deque()
        
        queue.append((root.left, root.right))
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                
                left, right = queue.pop()
                
                if (left and not right) or (right and not left):
                    return False
                
                elif not left and not right:
                    continue
                    
                else:
                    if left.val!= right.val:
                        return False
                    
                    queue.append((left.left, right.right))
                    
                    queue.append((left.right, right.left))
        
        return True
            