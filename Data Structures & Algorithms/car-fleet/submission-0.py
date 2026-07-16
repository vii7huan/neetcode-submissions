class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #position = [4,1,0,7], speed = [2,2,1,1], target = 10

        #pairs= [(7,1), (4,2), (1,2), (0,1)]
        #time  = (target - p) / s
        #stack = [3, 4.5, 10]

       
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for p,s in pairs:
            t = (target-p) /s
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)


