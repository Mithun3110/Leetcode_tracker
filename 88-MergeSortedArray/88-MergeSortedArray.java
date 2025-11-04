// Last updated: 11/4/2025, 10:05:22 AM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int r = m+n-1;
        int mi = m-1;
        int ni = n-1;
        while(ni >= 0){
            if(mi >= 0 && nums1[mi] > nums2[ni]){
                nums1[r] = nums1[mi];
                mi--;
                r--;
            }
            else{
                nums1[r] = nums2[ni];
                ni--;
                r--;
            }
        }
    }
}