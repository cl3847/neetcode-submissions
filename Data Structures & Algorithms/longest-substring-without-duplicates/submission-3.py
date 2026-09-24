class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        seen = set()
        seen.add(s[0])

        best = 0
        while right < len(s) - 1:
            right += 1
            c = s[right]

            if c in seen: 
                while not s[left] == c:
                    seen.remove(s[left])
                    left += 1
                left += 1
            
            seen.add(c)
            best = max(best, right-left + 1)
        return best



                