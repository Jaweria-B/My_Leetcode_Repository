# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        s, e = 0, len(inorder) -  1
        def helper(i, s, e):
            if i >= len(preorder) or s > e:
                return None
            
            element = preorder[i]
            idx = inorder.index(element)
            node = TreeNode(element)
            
            node.left = helper(i+1, s, idx-1)
            node.right = helper(i + (idx - s) + 1, idx + 1, e)
            return node
        return helper(i, s, e)
