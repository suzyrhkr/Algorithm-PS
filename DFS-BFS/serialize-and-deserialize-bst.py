# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        
        # bfs
        answer = []
        queue = [root]
        
        while queue:
            for node in queue:
                answer.append(str(node.val))
            
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

        return ",".join(answer)

        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        
        data = data.split(',')
        data = [int(x) for x in data]
        tree = TreeNode(data[0])
        
        for val in data[1:]:
            current_node = tree
      
            while True:
                if val < current_node.val:
                    if not current_node.left:
                        current_node.left = TreeNode(val)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = TreeNode(val)
                        break
                    else:
                        current_node = current_node.right
        return tree
                
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans