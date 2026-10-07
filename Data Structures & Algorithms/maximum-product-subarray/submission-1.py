class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = [1] * (len(nums) + 1)
        dp_max = [1] * (len(nums) + 1)

        for i in range(0, len(nums)):
            n = nums[i]
            
            a = n * dp_min[i]
            b = n * dp_max[i]
            c = n

            dp_min[i+1] = min(a, b, c)
            dp_max[i+1] = max(a, b, c)
        
        return max(dp_max[1:])

            
            

