class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    sol = [nums[i], nums[l], nums[r]]
                    if sol not in final:
                        final.append(sol)
                    l += 1
                    while l == l - 1:
                        l += 1
                    r -= 1
                    while r == r + 1:
                        r -= 1
                elif target > 0: # we should decrease the sum, move right closer
                    r -= 1
                else: # we should increase the sum, move left closer
                    l += 1
        return final

                


        