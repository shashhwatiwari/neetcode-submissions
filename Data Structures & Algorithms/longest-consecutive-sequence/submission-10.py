class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        track = {}
        longest = 1
        for num in nums:
            if num in track:
                continue
            else:
                track[num] = True
        for num in nums:
            if num-1 in track:
                continue # we do this because we see that current num cannot be the start 
                        # of the longest chain as there is a predecessor, so when we are at num we
                        # would at minumum be at a length of 2, hence this num is not what we process.

            curr = num # if num doesnt have any predecessor it could be the starting point of a seq.
            curr_len = 1
            while curr + 1 in track:
                curr = curr + 1
                curr_len += 1
            longest = max(longest,curr_len)
        return longest


        