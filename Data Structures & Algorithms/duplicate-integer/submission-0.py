class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            num_dict[i] = 0
        for i in nums:
            num_dict[i] += 1
            if num_dict[i] >1:
                return True
        return False