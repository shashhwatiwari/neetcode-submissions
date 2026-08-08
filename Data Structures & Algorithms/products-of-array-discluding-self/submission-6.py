class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if nums.count(0) == len(nums):
        #     return nums
        # runningprod = 1
        # zero_count = 0
        # for num in nums:
        #     if num != 0:
        #         runningprod *= num
        #     else:
        #         zero_count += 1
        # for i in range(len(nums)):
        #     if zero_count == 1:
        #         if nums[i] == 0:
        #             nums[i] = runningprod
        #         else:
        #             nums[i] = 0
        #     elif zero_count > 1:
        #         nums[i] = 0
        #     else:
        #         nums[i] = int(runningprod / nums[i])
        # return nums
        result = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix # we multiply with suffix only because we are finding product except self 
            suffix = suffix * nums[i]
        return result     
