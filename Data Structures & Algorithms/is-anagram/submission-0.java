class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> sFrequencies = new HashMap<>();
        HashMap<String, Integer> tFrequencies = new HashMap<>();

        for (int i = 0; i < s.length(); i += 1) {
            if (sFrequencies.containsKey(s.substring(i, i + 1))) {
                sFrequencies.put(s.substring(i, i + 1), sFrequencies.get(s.substring(i, i + 1)) + 1);
            }
            else {
                sFrequencies.put(s.substring(i, i + 1), 1);
            }
        }

        for (int i = 0; i < t.length(); i += 1) {
            if (tFrequencies.containsKey(t.substring(i, i + 1))) {
                tFrequencies.put(t.substring(i, i + 1), tFrequencies.get(t.substring(i, i + 1)) + 1);
            }
            else {
                tFrequencies.put(t.substring(i, i + 1), 1);
            }
        }

        return sFrequencies.equals(tFrequencies);
    }
}
