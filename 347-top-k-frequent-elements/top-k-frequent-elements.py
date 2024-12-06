# other techniques - Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num,cnt in count.items():
            freq[cnt].append(num)
        res = []    
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num) 
                if len(res) == k:
                    return res
# -------------------------------------------------------- #
# Brute force
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dict = {}
#         for num in nums:
#             if num in dict:
#                 dict[num] += 1
#             else:
#                 dict[num] = 1 
       
#         sorted_items = sorted(dict.items(), key = lambda x : x[1], reverse = True)
#         result = []
#         for n in sorted_items[:k]:
#             result.append(n[0])
#         return result  
# -------------------------------------------------------- #
# using counter
# freq_dict = Counter(arr)
# top_items = freq_dict.most_common(target)
# return top_items
# -------------------------------------------------------- #
