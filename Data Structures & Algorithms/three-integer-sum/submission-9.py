class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        
        res = []
        prev = None
        for i, n in enumerate(ns):
            if n > 0:
                break
            if n == prev:
                continue
            prev = n

            target = -n
            l = i + 1
            r = len(ns) - 1
            while l < r:
                s = ns[l] + ns[r]
                if s == target:
                    res.append((n, ns[l], ns[r]))
                    l += 1
                    r -= 1

                    # Skip duplicate second values
                    while l < r and ns[l] == ns[l - 1]:
                        l += 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res
