class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenArray = len(nums)
        arrayNoDups = set(nums)
        lenArrayNoDups = len(arrayNoDups)
        return lenArray != lenArrayNoDups
        