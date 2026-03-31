class Solution {
    public String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;
            
            // Extract numeric value if index is within bounds
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            
            // Append the remainder (0 or 1)
            res.append(sum % 2);
            // Update carry for the next position
            carry = sum / 2;
        }

        // The bits were added in reverse order (right-to-left)
        return res.reverse().toString();
    }
}
