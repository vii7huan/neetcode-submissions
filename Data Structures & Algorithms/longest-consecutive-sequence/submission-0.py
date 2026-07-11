class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = sorted(nums)
        best = 1
        cur = 1
        for i in range(len(new) - 1):        # stop before last index
            if new[i] == new[i + 1]:         # duplicate: skip, streak unchanged
                continue
            if new[i] + 1 == new[i + 1]:     # consecutive: extend streak
                cur += 1
                best = max(best, cur)
            else:                            # gap: reset streak
                cur = 1
        return best