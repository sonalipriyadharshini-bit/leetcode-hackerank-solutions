

class MyRegex {
    /* 
     * [01]?\\d{1,2} matches 0-199 (including leading zeros like 00, 01, 000)
     * 2[0-4]\\d     matches 200-249
     * 25[0-5]       matches 250-255
     */
    String zeroTo255 = "([01]?\\d{1,2}|2[0-4]\\d|25[0-5])";
    
    // We combine the pattern four times separated by literal dots
    public String pattern = zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255;
}
