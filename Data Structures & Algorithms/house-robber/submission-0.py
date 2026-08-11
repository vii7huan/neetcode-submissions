class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = cur = 0
        for n in nums:
            prev, cur = cur, max(cur, prev + n)
        return cur
