class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == len(nums):
            return nums
        runningprod = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                runningprod *= num
            else:
                zero_count += 1
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    nums[i] = runningprod
                else:
                    nums[i] = 0
            elif zero_count > 1:
                nums[i] = 0
            else:
                nums[i] = int(runningprod / nums[i])
        return nums
      
