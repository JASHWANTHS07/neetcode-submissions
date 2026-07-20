class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = set(nums)
        if len(nums)!=len(unq):
            return True
        else:
            return False
        