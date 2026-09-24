class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match c:
                case '(':
                    stack.append(c)
                case ')':
                    if stack:
                        element = stack.pop()
                        if not element == '(':
                            return False
                    else:
                        return False
                case '[':
                    stack.append(c)
                case ']':
                    if stack:
                        element = stack.pop()
                        if not element == '[':
                            return False
                    else:
                        return False
                case '{':
                    stack.append(c)
                case '}':
                    if stack:
                        element = stack.pop()
                        if not element == '{':
                            return False
                    else:
                        return False
                        
        return stack == []
        