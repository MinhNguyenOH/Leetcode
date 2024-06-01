class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_value = [[] for i in range(len(nums)+1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in count:
            freq_value[count[num]].append(num)
        
        res = []
        for i in range(len(freq_value)-1, 0, -1):
            for num in freq_value[i]:
                res.append(num)
                if len(res) == k:
                    return res