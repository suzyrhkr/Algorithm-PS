# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        #dfs 
        self.answer = 0
        def bst(node):
            if node:
                if L<= node.val <= R:
                    self.answer += node.val
                if L<node.val:
                    bst(node.left)
                if node.val<R:
                    bst(node.right)
        bst(root)
        return self.answer

