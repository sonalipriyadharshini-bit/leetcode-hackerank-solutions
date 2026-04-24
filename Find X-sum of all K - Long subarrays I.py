from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # sort by (frequency desc, value desc)
            items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            total = 0
            count = 0
            
            for val, f in items:
                if count < x:
                    total += val * f
                    count += 1
                else:
                    break
            
            res.append(total)
        
        return res
