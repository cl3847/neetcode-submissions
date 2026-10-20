class Solution:
    def canJump(self, nums: List[int]) -> bool:
        valid = [False] * len(nums)
        valid[0] = True
        for i, n in enumerate(nums):
            if valid[i]:
                for j in range(i + 1, i + n + 1):
                    if j < len(nums): valid[j] = True
        return valid[-1]