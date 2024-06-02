class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                total = n + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
        return res