class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, nums in enumerate(nums):
            if target - nums in hashtable:
                return [hashtable[target - nums], i]

            hashtable[nums] = i

        return []