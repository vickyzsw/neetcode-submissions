class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            n = nums[i]
            t = target - n
            if t in seen:
                if seen[t] < i:
                    return [seen[t], i]
                if seen[t] > i:
                    return [i,seen[t]]
            else:
                seen[n] = i

