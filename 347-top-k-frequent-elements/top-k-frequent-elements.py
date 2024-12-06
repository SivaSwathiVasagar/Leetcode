# Brute force
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1 
       
        sorted_items = sorted(dict.items(), key = lambda x : x[1], reverse = True)
        result = []
        for n in sorted_items[:k]:
            result.append(n[0])
        return result   