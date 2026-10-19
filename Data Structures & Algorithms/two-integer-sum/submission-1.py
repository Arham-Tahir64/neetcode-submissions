class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in idx:
                return [idx[rest], i]
            idx[nums[i]] = i



        