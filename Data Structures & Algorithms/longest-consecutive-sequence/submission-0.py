class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        best = 0
        for n in nums:
            if not n - 1 in nums_set:
                i = n
                while i in nums_set:
                    i += 1

                if i - n > best:
                    best = i - n
        
        return best
        