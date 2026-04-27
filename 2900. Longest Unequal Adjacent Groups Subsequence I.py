class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        ans = []
        last_group = -1
        
        for i in range(len(groups)):
            if groups[i] != last_group:
                ans.append(words[i])
                last_group = groups[i]
                
        return ans
