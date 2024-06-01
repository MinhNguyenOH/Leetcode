class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapp:
                return [mapp[diff], i]
            mapp[nums[i]] = i