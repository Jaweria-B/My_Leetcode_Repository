# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            if root:                
                leftSum = dfs(root.left)
                rightSum = dfs(root.right)
                
                if root.val >= low and root.val <= high:
                    return leftSum + rightSum + root.val
                else:
                    return leftSum + rightSum
            
        answer = dfs(root)
        
        return answer