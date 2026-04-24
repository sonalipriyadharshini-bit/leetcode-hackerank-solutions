from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit_count = [0] * 32
        
        def get_or():
            val = 0
            for i in range(32):
                if bit_count[i] > 0:
                    val |= (1 << i)
            return val
        
        left = 0
        res = float('inf')
        
        for right in range(n):
            # add nums[right]
            for i in range(32):
                if nums[right] & (1 << i):
                    bit_count[i] += 1
            
            # shrink window if OR ≥ k
            while left <= right and get_or() >= k:
                res = min(res, right - left + 1)
                
                # remove nums[left]
                for i in range(32):
                    if nums[left] & (1 << i):
                        bit_count[i] -= 1
                
                left += 1
        
        return res if res != float('inf') else -1
