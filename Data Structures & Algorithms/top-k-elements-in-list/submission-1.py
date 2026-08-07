class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        # using a bucket sort approach to find the top k frequency elements
        buckets = [[] for i in range(0,len(nums)+1)]
        for key, value in frequency.items():
            buckets[value].append(key) 
        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        
        