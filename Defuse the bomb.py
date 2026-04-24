from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # case 1: k == 0
        if k == 0:
            return [0] * n
        
        res = [0] * n
        
        # determine window direction
        start = 1 if k > 0 else n + k
        end = k if k > 0 else n - 1
        
        # initial window sum
        window_sum = 0
        for i in range(start, end + 1):
            window_sum += code[i % n]
        
        # sliding window
        for i in range(n):
            res[i] = window_sum
            
            # remove outgoing element
            window_sum -= code[start % n]
            
            # move window forward
            start += 1
            end += 1
            
            # add incoming element
            window_sum += code[end % n]
        
        return res
