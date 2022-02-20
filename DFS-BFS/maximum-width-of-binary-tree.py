# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        root.val = 0
        queue = [root]
        
        while queue:
            current_level = []
            max_width = max(max_width, queue[-1].val - queue[0].val + 1)
            for node in queue:
                if node.left:
                    node.left.val = 2*node.val
                    current_level.append(node.left)
                if node.right:
                    node.right.val = 2*node.val + 1
                    current_level.append(node.right)
            queue = current_level
                    
        return max_width