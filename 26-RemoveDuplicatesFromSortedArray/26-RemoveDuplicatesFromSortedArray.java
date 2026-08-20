// Last updated: 8/20/2026, 2:20:07 AM
class Solution {
    public int removeDuplicates(int[] nums) {
        var i = 0;
        for(int n: nums){
            if(i==0 || n > nums[i - 1]){
                nums[i++] = n;
            }
        }
        return i;
    }
}