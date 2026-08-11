class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)
        runningProd = 1
        if zeroCount > 1:
            for i in range(len(nums)):
                nums[i] = 0
        else:
            for num in nums:
                if num == 0:
                    continue
                else:
                    runningProd = runningProd * num
            print(f"runningProd is {runningProd}")
            if zeroCount == 0:
                for i in range(len(nums)):
                    nums[i] = int(runningProd / nums[i])
            else:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i] = runningProd
                    else:
                        nums[i] = 0
        return nums


        # result = [1] * len(nums)
        # prefix = 1
        # suffix = 1

        # for i in range(len(nums)):
        #     result[i] = prefix
        #     prefix = prefix * nums[i]
        
        # for i in range(len(nums) - 1, -1, -1):
        #     result[i] *= suffix # we multiply with suffix only because we are finding product except self 
        #     suffix = suffix * nums[i]
        # return result     
