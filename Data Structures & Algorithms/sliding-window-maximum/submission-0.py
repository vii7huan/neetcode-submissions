class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)-k + 1
        output = [0] * n
        for i in range(n):
            output[i] = max(nums[i:i+ k])
            i+= 1
        return output