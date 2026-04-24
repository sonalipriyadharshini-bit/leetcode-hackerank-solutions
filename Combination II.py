class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        
        def backtrack(remain, curr, start):
            if remain == 0:
                res.append(list(curr))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remain:
                    break
                
                curr.append(candidates[i])
                backtrack(remain - candidates[i], curr, i + 1)
                curr.pop()
                
        backtrack(target, [], 0)
        return res
