class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        newSet = set(nums)
        for num in newSet:
            if num-1 not in newSet:
                curNum = num
                curLength = 1
                while curNum+1 in newSet:
                    curNum += 1 
                    curLength += 1
                res = max(res, curLength)
        return res        
