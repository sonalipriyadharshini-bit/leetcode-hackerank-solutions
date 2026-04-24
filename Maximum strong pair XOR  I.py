class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(20, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1
    
    def remove(self, num):
        node = self.root
        for i in range(20, -1, -1):
            bit = (num >> i) & 1
            next_node = node.children[bit]
            next_node.count -= 1
            node = next_node
    
    def max_xor(self, num):
        node = self.root
        res = 0
        for i in range(20, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if toggled in node.children and node.children[toggled].count > 0:
                res |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children.get(bit, node)
        return res


class Solution:
    def maximumStrongPairXor(self, nums):
        nums.sort()
        trie = Trie()
        left = 0
        max_xor = 0
        
        for right in range(len(nums)):
            # add current number
            trie.insert(nums[right])
            
            # shrink window
            while nums[right] > 2 * nums[left]:
                trie.remove(nums[left])
                left += 1
            
            # query max XOR
            max_xor = max(max_xor, trie.max_xor(nums[right]))
        
        return max_xor
