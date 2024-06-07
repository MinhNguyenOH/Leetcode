class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num = float('inf')
        while l <= r:
            m = (l+r)//2
            min_num = min(nums[m], min_num)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(min_num, nums[l])