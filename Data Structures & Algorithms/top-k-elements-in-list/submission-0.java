class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer>[] freqs = new List[nums.length + 1];

        for (int i = 0; i < freqs.length; i += 1) {
            freqs[i] = new ArrayList<>();
        }

        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            freqs[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freqs.length - 1; i > 0; i -= 1) {
            for (int num : freqs[i]) {
                res[index] = num;
                index++;

                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
