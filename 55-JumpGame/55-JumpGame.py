class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr = 0
        n = len(nums)
        for i in range(n):
            if i>maxr:
                return False
            maxr = max(maxr,i+nums[i])
            if maxr >= n-1:
                return True

        return False