class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 0:
            return True
        s = s.replace(" ", "")
        new = "".join(char for char in s if char.isalnum())
        new = new.upper()
        left, right = 0, len(new)-1
        if len(new) <= 1:
            return True
        while left < right:
            if new[left] == new[right]:
                left += 1
                right -= 1
            else:
                return False
        return True