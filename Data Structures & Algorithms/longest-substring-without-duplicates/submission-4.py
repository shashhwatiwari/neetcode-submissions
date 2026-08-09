class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # left = 0
        # right = 0
        # counter = 1
        # maxCount = 1
        # seen = {}
        # while right < len(s):
        #     if s[right] not in seen:
        #         seen[s[right]] = right
        #         right += 1
        #         counter = right - left
        #     else:
        #         left = max(left, seen[s[right]] + 1)
        #         seen[s[right]] = right
        #         right += 1
        #         counter = right - left
        #     maxCount = max(counter, maxCount)
        # return maxCount
        count = 0
        seen = set()
        left = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                count = max(count, i - left + 1)
            else:
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[i])
        return count

            

 



            

        