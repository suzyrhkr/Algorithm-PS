class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer, path = [], []
        
        def backtracking(src, des):         
            if src == des:
                answer.append(path[:])
                return
            
            for node in graph[src]:
                path.append(node)
                backtracking(node, des)
                path.pop()                  
            return
        
        path.append(0)
        backtracking(0, len(graph)-1)
        
        return answer

        