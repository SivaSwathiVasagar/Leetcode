class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            if num > 0 :
                break
            if index > 0 and num == nums[index -1]:
                continue
            l , r = index + 1, len(nums) - 1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result                





# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             if i != 0 and nums[i] == nums[i-1]:
#                 continue
#             target = -nums[i]
#             l,r = i+1, len(nums)-1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     res.append([-target, nums[l], nums[r]])
#                     r -= 1
#                     l += 1
#                     while l < r and nums[r] == nums[r+1]: r -= 1
#                     while l < r and nums[l] == nums[l-1]: l += 1
#                 elif nums[l] + nums[r] > target:
#                     r -= 1
#                 else:
#                     l += 1
#         return res