# Last updated: 11/4/2025, 10:05:29 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff],i]
            map[n] = i
        return
         
        