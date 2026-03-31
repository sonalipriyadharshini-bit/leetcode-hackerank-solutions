class Solution {
    public int strStr(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();

        // If needle is longer than haystack, it can't be a match
        if (nLen > hLen) return -1;

        // Loop through haystack, stopping where needle wouldn't fit anymore
        for (int i = 0; i <= hLen - nLen; i++) {
            // Check if the substring starting at 'i' matches the needle
            if (haystack.substring(i, i + nLen).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}

