class Solution:
    def findMin(self, nums: List[int]) -> int:
        globMin = 10000
        for num in nums:
            globMin = min(globMin, num)
        return globMin