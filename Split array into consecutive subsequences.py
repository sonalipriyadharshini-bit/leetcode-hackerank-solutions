class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Step 1: Count frequency of all numbers
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
                
        # Step 2: Track sequences that can be extended
        # end[n] = number of sequences ending at n-1 (waiting for n)
        end = {}
        
        for n in nums:
            # If we've already used all instances of this number, skip it
            if count[n] == 0:
                continue
                
            # Case 1: Try to append n to an existing sequence ending at n-1
            if n in end and end[n] > 0:
                count[n] -= 1
                end[n] -= 1
                # This sequence now ends at n, so it's waiting for n+1
                if (n + 1) in end:
                    end[n + 1] += 1
                else:
                    end[n + 1] = 1
                    
            # Case 2: Try to start a new sequence [n, n+1, n+2]
            elif (n + 1) in count and count[n + 1] > 0 and \
                 (n + 2) in count and count[n + 2] > 0:
                count[n] -= 1
                count[n + 1] -= 1
                count[n + 2] -= 1
                # This new sequence now ends at n+2, waiting for n+3
                if (n + 3) in end:
                    end[n + 3] += 1
                else:
                    end[n + 3] = 1
            
            # Case 3: Cannot extend or start a valid sequence
            else:
                return False
                
        return True
