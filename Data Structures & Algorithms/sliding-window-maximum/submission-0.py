class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = nums[:k]
        maxlist = []
        maxlist.append(max(arr))
        for r in range(k,len(nums)):
            arr.append(nums[r])
            arr.pop(0)
            maxlist.append(max(arr))
        return maxlist