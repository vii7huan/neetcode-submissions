class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Input: nums = [7,7], k = 1 Output: [7]
        #nums = [1,2,2,3,3,3], k = 2 Output: [2,3]
        count = Counter(nums)                          # {1:1, 2:2, 3:3}
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]
        
