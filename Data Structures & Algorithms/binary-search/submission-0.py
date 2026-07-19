class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, s in enumerate(nums):
            if target == s:
                return i
            i += 1
            if i == len(nums) and target!= s:
                return -1
            
