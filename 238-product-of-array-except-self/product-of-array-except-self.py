class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = post = 1
        for num in range(len(nums)):
            res[num] = pre
            pre = pre * nums[num]
        for num in range(len(nums)-1, -1, -1):
            res[num] *= post
            post = post * nums[num]
        return res   
    #---------------------------------# 
    # with division logic
        # target = 0
        # prod = 1
        # res = []
        # for num in range(len(nums)):
        #     target = nums[num]
        #     prod = prod * target
        # for num in range(len(nums)):  
        #     res.append(prod // nums[num])
        # return res 
    #---------------------------------# 
                       



   

            
        