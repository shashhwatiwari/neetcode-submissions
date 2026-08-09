class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: # we add index AFTER checking if it exists so each time we check from things we know of
                return [seen[diff], i]
            seen[num] = i 
            




