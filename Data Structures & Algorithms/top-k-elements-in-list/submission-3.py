class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        max_list = []
        for num in nums:
            num_dict[num] = 0
        for num in nums:
            num_dict[num] += 1
        
        for i in range(k):
            current_max = -9999999
            current_max_index = -999999
            for num in num_dict:
                if num not in max_list:
                    if num_dict[num] > current_max:
                        current_max = num_dict[num]
                        current_max_index = num
            max_list.append(current_max_index)
        return max_list

        