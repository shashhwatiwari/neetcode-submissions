class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # for iterations after the first one to see if we have processed the same number already.
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    sol = [nums[i], nums[left], nums[right]]
                    if sol not in res:
                        res.append(sol)
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1                    
        return res

                


        