import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        a=[0] * n
        for i in range(len(nums)):
            if nums[i]!= 0:
                prods = int(math.prod(nums)/nums[i])
            else:
                neww = nums.copy()
                neww.remove(0)
                prods = int(math.prod(neww))
            a[i] = prods
        return a
            
                    