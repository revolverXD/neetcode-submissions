class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        fast = 0
        slow = 0
        while fast  < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow