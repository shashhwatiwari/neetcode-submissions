class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 0:
            return True
        else:
            s = s.replace(" ", "")
            s = "".join(char for char in s if char.isalnum()).lower()
            l, r = 0, len(s) - 1
            print(s)
            while l < r:
                if s[l] == s[r] :
                    l += 1
                    r -= 1
                else:
                    return False
            return True