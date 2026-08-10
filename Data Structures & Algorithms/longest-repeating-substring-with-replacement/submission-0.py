class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maxFreq(counter):
            return max(counter.values())
        
        freq = {}
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            #while window is overshooting the value K we move left pointer to come in range
            while (i - l + 1) - maxFreq(freq) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res,(i - l + 1))
        return res
            
                    
                

                    

            

        