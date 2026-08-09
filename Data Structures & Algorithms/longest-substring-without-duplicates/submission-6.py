class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        # count = 0
        # seen = set()
        # left = 0
        # for i in range(len(s)):
        #     if s[i] not in seen:
        #         seen.add(s[i])
        #         count = max(count, i - left + 1)
        #     else:
        #         while s[i] in seen:
        #             seen.remove(s[left])
        #             left += 1
        #         seen.add(s[i])
        # return count
        
        count = 0
        res = 0
        seen = {}
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]] = right
                count += 1
            else:
                left = max(left, seen[s[right]]+1)
                seen[s[right]] = right
                count = right - left + 1
            res = max(count, res)
        return res


            

 



            

        