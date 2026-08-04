class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        track = {}
        for char in s:
            if char in track:
                track[char] += 1
            else:
                track[char] = 1
        for char in t:
            if char in track:
                track[char] -= 1
            else:
                return False
        for value in track.values():
            if value > 0:
                return False
        return True 
        