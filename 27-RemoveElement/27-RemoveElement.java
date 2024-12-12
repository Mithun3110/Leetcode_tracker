class Solution {
    public int removeElement(int[] nums, int val) {
        int i =0;
        int l = nums.length;
        int r =0;
        int k=0;
        for(int j=0;j<l;j++){
            if(nums[j]!=val){
                nums[k] = nums[j];
                k++;
                r++;
            }
        }
        return r;
    }
}