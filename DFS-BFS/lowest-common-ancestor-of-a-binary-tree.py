# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p, q):
        if not node:
            return None
        
        if node in [p, q]:
            return node
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right:
            return node
        if left:
            return left
        elif right:
            return right
        else: 
            return None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
        