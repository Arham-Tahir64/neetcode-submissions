class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        if len(nums) == 0:
            return False
        for n in nums:
                if n in my_dict:
                    my_dict[n] += 1
                else:
                    my_dict[n] = 1
        max_key = max(my_dict, key=my_dict.get)
        if my_dict[max_key] > 1:
            return True
        return False