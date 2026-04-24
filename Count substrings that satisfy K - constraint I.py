class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        count0 = count1 = 0
        result = 0
        
        for right in range(len(s)):
            if s[right] == '0':
                count0 += 1
            else:
                count1 += 1
            
            # shrink window if invalid
            while count0 > k and count1 > k:
                if s[left] == '0':
                    count0 -= 1
                else:
                    count1 -= 1
                left += 1
            
            # all substrings ending at right are valid
            result += (right - left + 1)
        
        return result
