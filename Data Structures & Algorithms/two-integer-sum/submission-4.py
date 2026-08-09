class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: # we add index AFTER checking if it exists so each time we check from things we know of
                return [seen[diff], i]
            seen[num] = i 
            # lets say we have [3,0,1,3,2,4] and target is 6. we add 3 at i = 0 and then we we get to 3 at i = 3, since its not in the list of seen items it doesnt 




