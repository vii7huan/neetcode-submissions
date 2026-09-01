class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 0
        # for _ in range(32):
        #     res = (res<< 1) | (n & 1)
        #     n >>= 1
        # return res

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res