class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for c in s:
            s1[c] = s1.get(c, 0) + 1
        for c in t:
            s2[c] = s2.get(c, 0) + 1

        return s1 == s2
        