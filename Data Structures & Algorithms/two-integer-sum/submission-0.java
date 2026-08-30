class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> complements = new HashMap<>();

        for (int i = 0; i < nums.length; i += 1) {
            if (!complements.containsKey(nums[i])) {
                complements.put(target - nums[i], i);
            }
            else {
                result[0] = complements.get(nums[i]);
                result[1] = i;

                return result;
            }
        }

        return result;
    }
}
