class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1  # 2147483647
        MIN_INT = -2**31    # -2147483648
        
        res = 0
        # Determine sign and work with absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating res
            # (res * 10 + pop) > MAX_INT  =>  res > (MAX_INT - pop) / 10
            if res > (MAX_INT - pop) // 10:
                return 0
                
            res = res * 10 + pop
            
        return res * sign
