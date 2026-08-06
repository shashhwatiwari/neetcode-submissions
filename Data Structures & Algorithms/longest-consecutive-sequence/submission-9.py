class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force scans through the entire nums at every iteration
        # longest_seq = 0
        # for i in range(len(nums)):
        #     temp = [nums[i]]
        #     seq = nums[i]
        #     for k in range(i+1,len(nums)):
        #         if nums[k] - seq == 1:
        #             temp.append(nums[k])
        #             seq = nums[k]
        #         else:
        #             continue
        #     longest_seq = max(longest_seq,len(temp))
        # return longest_seq   
        # correction ^ this is for sequential consecutive elements

        # brute force with the actual question process - sort and then do what you did before. 
        # nums = sorted(nums) 
        # longest_seq = 0
        # for i in range(len(nums)):
        #     temp = [nums[i]]
        #     seq = nums[i]
        #     for k in range(i+1,len(nums)):
        #         if nums[k] - seq == 1:
        #             temp.append(nums[k])
        #             seq = nums[k]
        #         else:
        #             continue
        #     longest_seq = max(longest_seq,len(temp))
        # return longest_seq 

        # a better approach could potentially be, scan the array and keep a hashmap of their counts or wtv
        #scan it again, for each "nums[i]" check if nums[i] + 1 exists in the hashmap, if so, update the 
        
        # if not nums:
        #     return 0
        # track = {}
        # for num in nums:
        #     if num in track:
        #         continue
        #     else:
        #         track[num] = 1
        # maxCount = 0
        # lenCount = 0
        # seq_head = nums[0]
        # for i in range(len(nums)-1):
        #     if seq_head+1 in track:
        #         lenCount += 1
        #         seq_head += 1 
        #     else:
        #         seq_head = nums[i+1]
        #         maxCount = max(maxCount, lenCount)
        #         lenCount = 0
        # maxCount = max(maxCount, lenCount)
        # return maxCount + 1
        # Does not work ^ a lot of edge cases, cannot capture the sequence, rather just increments

        # Solution
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


        