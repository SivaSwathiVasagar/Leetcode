class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = nums
        if len(s) == len(set(s)):
            return False
        else:
            return True

       



