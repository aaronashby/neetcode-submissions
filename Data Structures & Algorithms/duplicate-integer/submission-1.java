class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> frequencies = new HashMap<>();

        for (Integer num : nums) {
            if (frequencies.containsKey(num)) {
                return true;
            }
            else {
                frequencies.put(num, 1);
            }
        }

        return false;
    }
}