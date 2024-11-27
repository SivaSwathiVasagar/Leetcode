class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenlist = []
        digits = " "
        for num in nums:
            digits = str(num)
            if len(digits)%2 == 0:
                evenlist.append(num)
        return len(evenlist)      

            