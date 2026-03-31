import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        // 1. Sort the array to bring the most different strings to the ends
        Arrays.sort(strs);
        
        String first = strs[0];
        String last = strs[strs.length - 1];
        int i = 0;
        
        // 2. Compare only the first and last strings
        while (i < first.length() && i < last.length()) {
            if (first.charAt(i) == last.charAt(i)) {
                i++;
            } else {
                break;
            }
        }
        
        // 3. The matching part is the prefix for all strings
        return first.substring(0, i);
    }
}

