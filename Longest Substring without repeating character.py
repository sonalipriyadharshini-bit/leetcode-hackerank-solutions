class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        max_length = 0
        start = 0
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = right
            max_length = max(max_length, right - start + 1)
        return max_length
