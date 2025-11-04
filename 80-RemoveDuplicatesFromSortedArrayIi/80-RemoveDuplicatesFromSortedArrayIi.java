// Last updated: 11/4/2025, 10:05:23 AM
class Solution {
    public int removeDuplicates(int[] nums) {
        int k=2;
        int i=2;
        int r=2;
        while(i<nums.length){
            if(nums[i]!=nums[k-2]){
                nums[k]=nums[i];
                k++;
                r++;
            }
            i++;
        }  
        return r;      
    }
}