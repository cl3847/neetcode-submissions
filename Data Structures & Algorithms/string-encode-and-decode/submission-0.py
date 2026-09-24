class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        while not s == "":
            i = s.index("#")
            length = int(s[:i])
            next = s[i+1:i+length+1]
            s = s[i+length+1:]
            strs.append(next)
        return strs
        