# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def inorder(root):
            nonlocal ans
            nonlocal k
            if root:
                inorder(root.left)
                if k == 1:
                    ans = root.val
                    k = 0
                    return
                else:
                    k -= 1
                    
                inorder(root.right)
                
        inorder(root)
        return ans