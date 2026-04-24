class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Step 1: count whites in first window
        white_count = blocks[:k].count('W')
        min_ops = white_count
        
        # Step 2: slide window
        for i in range(k, len(blocks)):
            # add new char
            if blocks[i] == 'W':
                white_count += 1
            
            # remove old char
            if blocks[i - k] == 'W':
                white_count -= 1
            
            min_ops = min(min_ops, white_count)
        
        return min_ops
