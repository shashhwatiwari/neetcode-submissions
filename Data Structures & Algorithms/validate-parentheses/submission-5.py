class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        else:
            for i in range(len(s)):
                if s[i] in pairs:
                    stack.append(s[i])
                else:
                    if stack and pairs[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
            if not stack:
                return True
            else:
                return False
                    

        