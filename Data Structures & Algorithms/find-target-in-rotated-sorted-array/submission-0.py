class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
#Input: nums = [3,5,6,0,1,2], target = 4 Output: -1
#Input: nums = [3,4,5,6,1,2], target = 1 Output: 4

        while l<= r:
            m = (l + r)//2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m+ 1
                else:
                    r = m -1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m + 1
        return -1