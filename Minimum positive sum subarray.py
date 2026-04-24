from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        
        # prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        ans = float('inf')
        
        # try all subarrays
        for i in range(n):
            for length in range(l, r + 1):
                if i + length <= n:
                    sub_sum = prefix[i + length] - prefix[i]
                    
                    if sub_sum > 0:
                        ans = min(ans, sub_sum)
        
        return ans if ans != float('inf') else -1
