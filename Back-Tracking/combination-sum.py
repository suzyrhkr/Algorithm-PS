class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer, combination = [], []
        
        def backtracking(idx):
            cur_sum = sum(combination)
            if target < cur_sum:
                return
            elif cur_sum == target:
                    answer.append(combination.copy())
                    return
            
            for i in range(idx,len(candidates)):
                combination.append(candidates[i])
                backtracking(i)
                combination.pop()
            return
        
        backtracking(0)
        return answer