class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * n

        if n < 2:
            return 1

        res[0] = 1
        res[1] = 2

        i = 2
        while i < n:
            res[i] = res[i-1] + res[i-2]
            i += 1
            print(res)

        return res[-1]