class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        length = len(nums)
        fast = 1
        slow = 0 
        while fast < length:
            if nums[fast] != nums[slow]:
                slow +=1
                nums[slow] = nums[fast]
            fast +=1
        return slow + 1