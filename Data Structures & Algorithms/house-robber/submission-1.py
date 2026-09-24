from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def robrec(i):
            if i >= len(nums):
                return 0
            return max(
                robrec(i + 1),
                robrec(i + 2) + nums[i]
                )
        
        return robrec(0)
