class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif pairs[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


        