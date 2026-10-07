class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            hm.put(target-n, i);
        }

        for (int i = 0; i < nums.length; i++) {
            Integer match = hm.get(nums[i]);
            if (match != null && match != i) {
                return new int[]{i, match};
            }
        }

        return null;
    }
}
