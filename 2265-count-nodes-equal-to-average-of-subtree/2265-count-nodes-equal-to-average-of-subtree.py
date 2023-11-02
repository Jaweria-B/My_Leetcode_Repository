# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        
        def postOrder(root):
            nonlocal count
            
            if root == None:
                return [0, 0]
            
            leftSum, lCnt = postOrder(root.left)
            rightSum, rCnt = postOrder(root.right)
            
            nodeSum = leftSum + rightSum + root.val
            nodeCount = lCnt + rCnt + 1
            
            if nodeSum // nodeCount == root.val:
                count += 1
            
            return [nodeSum, nodeCount]
        
        postOrder(root)
        
        return count