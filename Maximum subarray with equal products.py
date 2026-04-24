from typing import List
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1
        
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            
            for j in range(i, n):
                prod *= nums[j]
                
                # update gcd
                g = nums[j] if j == i else math.gcd(g, nums[j])
                
                # update lcm
                l = nums[j] if j == i else (l * nums[j]) // math.gcd(l, nums[j])
                
                if prod == g * l:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
