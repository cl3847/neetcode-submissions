from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        i = 2
        while i < len(nums):
            res[i] = max(
                res[i - 1],
                res[i - 2] + nums[i]
            )
            i += 1
        
        return max(res[-1], res[-2])
