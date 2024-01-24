# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0
        
        def dfs(curr):
            nonlocal odd
            if not curr:
                return 0
            
            count[curr.val] += 1
            odd_change = 1 if count[curr.val] % 2 == 1 else -1
            odd += odd_change
            
            if not curr.left and not curr.right:
                res = 1 if odd <= 1 else 0
            else:
                res = dfs(curr.left) + dfs(curr.right)
                
            odd -= odd_change
            count[curr.val] -= 1
            
            return res
        
        return dfs(root)