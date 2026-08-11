class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        final, counter = 0, 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            counter = r - l + 1
            while (r - l + 1) - max(freq.values()) > k:
                final = max(final, counter - 1)
                freq[s[l]] -= 1
                l += 1
        return max(final, r - l + 1)
                
        
            
                    
                

                    

            

        