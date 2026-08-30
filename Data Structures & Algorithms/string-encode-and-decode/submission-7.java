class Solution {
    public String encode(List<String> strs) {
        String encoded = "";

        for (String str : strs) {
            encoded = encoded + str.length() + "#" + str;
        }

        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            int j = i;

            while (str.charAt(j) != '#') {
                j++;
            }

            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            decoded.add(str.substring(i, j));

            i = j;
        }

        return decoded;
    }
}
