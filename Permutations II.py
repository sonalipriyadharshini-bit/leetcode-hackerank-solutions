from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = Counter(nums)
        
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(list(curr))
                return
            
            for n in counts:
                if counts[n] > 0:
                    curr.append(n)
                    counts[n] -= 1
                    
                    backtrack(curr)
                    
                    counts[n] += 1
                    curr.pop()
        
        backtrack([])
        return res
