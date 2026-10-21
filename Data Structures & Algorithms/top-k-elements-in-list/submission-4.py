from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        most_common = nums_dict.most_common()
        out = []
        for i in range(k):
            out.append(most_common[i][0])
        return out