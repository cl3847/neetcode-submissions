class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ms = {}
        for s in strs:
            m = [0] * 26
            for c in s:
                m[ord(c) - 97] += 1
            v = ms.get(tuple(m), [])
            v.append(s)
            ms[tuple(m)] = v
        return list(ms.values())