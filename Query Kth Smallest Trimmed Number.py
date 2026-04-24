from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        
        for k, trim in queries:
            arr = []
            
            # Step 1: trim numbers
            for i, num in enumerate(nums):
                trimmed = num[-trim:]  # rightmost digits
                arr.append((trimmed, i))
            
            # Step 2: sort (string compare works correctly)
            arr.sort()
            
            # Step 3: pick k-th smallest
            res.append(arr[k-1][1])
        
        return res
