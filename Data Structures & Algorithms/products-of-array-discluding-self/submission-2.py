import math
def product_array(num):
    val = math.prod(num)
    return val


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        if len(nums)>0:
            for i in range(len(nums)):
                numss=nums.copy()
                numss.pop(i) 
                a.append(product_array(numss))
        return a
                    