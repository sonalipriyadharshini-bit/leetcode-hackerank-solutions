class Solution {
    // Memoization table to store results
    Boolean[][] memo;

    public boolean isMatch(String s, String p) {
        memo = new Boolean[s.length() + 1][p.length() + 1];
        return dp(0, 0, s, p);
    }

    private boolean dp(int i, int j, String s, String p) {
        if (memo[i][j] != null) return memo[i][j];

        boolean result;
        // Base case: if we reach the end of the pattern
        if (j == p.length()) {
            result = (i == s.length());
        } else {
            // Check if the first characters match
            boolean firstMatch = (i < s.length() && 
                                 (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.'));

            // Handle the '*' wildcard logic
            if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                // Option 1: Skip '*' and the preceding char (match zero elements)
                // Option 2: Use '*' if firstMatch is true (move to next char in s)
                result = dp(i, j + 2, s, p) || 
                         (firstMatch && dp(i + 1, j, s, p));
            } else {
                // No '*' nearby, just move both pointers forward if they match
                result = firstMatch && dp(i + 1, j + 1, s, p);
            }
        }

        memo[i][j] = result;
        return result;
    }
}

