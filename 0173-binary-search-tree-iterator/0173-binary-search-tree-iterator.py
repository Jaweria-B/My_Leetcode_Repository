# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.travarsel = []
        self.inorder(root)
        self.current = 0
        

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.travarsel.append(root.val)
            self.inorder(root.right)
        
    def next(self) -> int:
        if self.current < len(self.travarsel):
            pointer = self.current
            self.current += 1
            return self.travarsel[pointer]

    def hasNext(self) -> bool:
        if self.current < len(self.travarsel):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()