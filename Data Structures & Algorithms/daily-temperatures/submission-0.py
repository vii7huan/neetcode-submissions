class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        stack = []

        # temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
        #stack = [(73,0),] ->[]
        #res = [1,0,0,0,0,0,0,0]

        for i ,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackt, stackind = stack.pop()
                res[stackind] = i - stackind
            stack.append((t,i))
        return res

            