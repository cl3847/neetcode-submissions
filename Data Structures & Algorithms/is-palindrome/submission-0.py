class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        s = s.lower()

        while p1 < p2:
            if not s[p1].isalpha() and not s[p1].isdigit():
                p1 += 1
                continue
            elif not s[p2].isalpha() and not s[p2].isdigit():
                p2 -= 1
                continue
            
            if not s[p1] == s[p2]:
                return False
            
            print(s[p1], s[p2])

            p1 += 1
            p2 -= 1
            
        return True