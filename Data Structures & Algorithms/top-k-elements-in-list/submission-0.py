class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = [[] for _ in range(len(nums) + 1)]
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for key, v in d.items():
            a[v].append(key)

        i = len(nums)
        res = []
        while i >= 0 and len(res) < k:
            if not a[i] == []:
                res.extend(a[i])
            i -= 1
        return res