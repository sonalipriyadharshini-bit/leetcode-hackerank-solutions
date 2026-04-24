class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def solve(sub):
            if len(sub) < 2:
                return ""
            
            char_set = set(sub)
            
            for i, ch in enumerate(sub):
                # if pair doesn't exist → split
                if ch.swapcase() not in char_set:
                    left = solve(sub[:i])
                    right = solve(sub[i+1:])
                    
                    return left if len(left) >= len(right) else right
            
            # valid nice substring
            return sub
        
        return solve(s)
