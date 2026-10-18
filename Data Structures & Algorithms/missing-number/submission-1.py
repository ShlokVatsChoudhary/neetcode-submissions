class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        length = len(nums)
        summ = sum(range(length + 1))

        return summ - total