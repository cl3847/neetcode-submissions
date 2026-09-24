class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        for n in nums:
            prefix.append(prefix[-1] * n)
        
        for n in nums[::-1]:
            suffix.append(suffix[-1] * n)

        suffix = suffix[::-1]
        return [prefix[i] * suffix[i+1] for i, n in enumerate(nums)]