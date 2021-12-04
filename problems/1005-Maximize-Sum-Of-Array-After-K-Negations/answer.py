class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums_len = len(nums)

        i = 0
        j = k
        while i < j:
            if nums[i] < 0:
                nums[i] = -nums[i]
                if i != j - 1 and (i != nums_len - 1 and nums[i] >= nums[i + 1]):
                    i += 1
                else:
                    j -= 1
            elif nums[i] == 0:
                return sum(nums)
            elif nums[i] > 0:
                if ((j - i) % 2 != 0):
                    nums[i] = -nums[i]
                    return sum(nums)
                else:
                    return sum(nums)
        return sum(nums)