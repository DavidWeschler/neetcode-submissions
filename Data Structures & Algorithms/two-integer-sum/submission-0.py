class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, num in enumerate(nums):
            complete = target - num
            if complete in hashmap:
                return [hashmap[complete], index]
            hashmap[num] = index
