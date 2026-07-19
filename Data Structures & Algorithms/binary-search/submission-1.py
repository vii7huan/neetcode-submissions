class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #direct
        #for i, s in enumerate(nums):
        #    if target == s:
        #        return i
        #    i += 1
        #    if i == len(nums) and target!= s:
        #        return -1
        

        #1,2,3,4,5
        l,r = 0, len(nums)
        
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1
