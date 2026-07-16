class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #stack = [(i,height)]
        #heights = [7,1,7,2,2,4]
        #stack=[(7,1)]

        #first look at each bars, then finally for the whole distance
        
        stack =[]
        maxa = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxa = max(maxa,height * (i - index))
                start = index
            stack.append((start, h))
        

        for i , h in stack:
            maxa = max(maxa,h* (len(heights)- i ))
        return maxa
