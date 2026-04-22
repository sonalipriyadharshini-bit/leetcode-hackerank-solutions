class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(remain, curr, start):
            if remain == 0:
                res.append(list(curr))
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(remain - candidates[i], curr, i)
                curr.pop()
        
        backtrack(target, [], 0)
        return res
