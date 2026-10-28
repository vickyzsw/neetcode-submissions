class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for m in nums:
            if m in count:
                count[m] += 1
            else:
                count[m]=1
        orderd = sorted(count, key = count.get, reverse = True)
        return orderd[:k]
