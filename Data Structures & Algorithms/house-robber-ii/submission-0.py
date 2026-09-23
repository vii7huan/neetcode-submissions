class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob(arr):
            prev = cur =0
            for n in arr:
                prev,cur= cur,max(cur, prev+n)
            return cur
        return max(rob(nums[1:]), rob(nums[:-1]))