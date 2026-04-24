from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        max_len = 0
        
        i = 0
        while i < n:
            # start only if valid (even and <= threshold)
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1
                j = i
                
                # expand while conditions hold
                while j + 1 < n and nums[j + 1] <= threshold and (nums[j] % 2 != nums[j + 1] % 2):
                    length += 1
                    j += 1
                
                max_len = max(max_len, length)
                i = j + 1  # jump forward
            else:
                i += 1
        
        return max_len
