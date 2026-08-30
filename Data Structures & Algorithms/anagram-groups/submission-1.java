class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for (String str : strs) {
            int[] frequencies = new int[26];
            for (char c : str.toCharArray()) {
                frequencies[c - 'a'] += 1;
            }

            String key = Arrays.toString(frequencies);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(str);
        }

        return new ArrayList<>(res.values());
    }
}
