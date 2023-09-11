# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        if not root:
            return ans
        
        queue = collections.deque([root])
        
        forward = False
        
        while queue:
            temp = []
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            forward = not forward
            
            if forward:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            
        return ans