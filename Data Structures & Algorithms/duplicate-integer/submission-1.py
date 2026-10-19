from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for n in counter:
            if counter[n] > 1:
                return True
        return False