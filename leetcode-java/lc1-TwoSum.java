class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> cache = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (cache.get(nums[i]) != null){
                return new int[] {i, cache.get(nums[i])};
            }
            else{
                cache.put(target-nums[i], i);
            }
        }
        return null;
    }
}
