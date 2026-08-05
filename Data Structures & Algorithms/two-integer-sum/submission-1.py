class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num # gives us the number we want
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

