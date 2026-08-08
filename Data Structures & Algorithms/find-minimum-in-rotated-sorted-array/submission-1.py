class Solution:
    def findMin(self, nums: List[int]) -> int:
        # globMin = 10000
        # for num in nums:
        #     globMin = min(globMin, num)
        # return globMin
        if len(nums) == 1:
            return nums[0]
        else:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (right + left)// 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid 
            return nums[left]

