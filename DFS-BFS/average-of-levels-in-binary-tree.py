# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:        
        queue = [root]
        answer = []
        
        while queue:
            level_sum = 0
            for node in queue:
                level_sum += node.val
     
            answer.append(level_sum/float(len(queue)))
        
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = []
            
            if tmp:
                for node in tmp:
                    queue.append(node)
            
        return answer
            
            
                
            