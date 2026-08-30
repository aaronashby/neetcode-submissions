class Solution {
    public String encode(List<String> strs) {
        String encoded = "";

        for (int i = 0; i < strs.size(); i += 1) {
            encoded = encoded + strs.get(i) + ";-";
        }

        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        int startingIndex = 0;

        for (int i = 0; i < str.length() - 1; i += 1) {
            if (str.charAt(i) == ';' && str.charAt(i + 1) == '-') {
                decoded.add(str.substring(startingIndex, i));
                startingIndex = i + 2;
            }
        }

        return decoded;
    }
}
