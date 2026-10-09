class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        new_arr = []
        for i in range(length):
            new_arr.append(nums[i])

        for i in range(length, 2*length):
            new_arr.append(nums[i-length])

        nums = new_arr
        return nums