class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> anagrams = new HashMap<>();
        List<List<String>> res = new ArrayList<>();

        for (int i = 0; i < strs.length; i += 1) {
            char[] currString = strs[i].toCharArray();
            Arrays.sort(currString);

            if (anagrams.containsKey(new String(currString))) {
                anagrams.get(new String(currString)).add(strs[i]);
            }
            else {
                ArrayList<String> emptyAnagrams = new ArrayList<>();
                emptyAnagrams.add(strs[i]);
                anagrams.put(new String(currString), emptyAnagrams);
            }
        }

        for (ArrayList<String> group : anagrams.values()) {
            res.add(group);
        }

        return res;
    }
}
