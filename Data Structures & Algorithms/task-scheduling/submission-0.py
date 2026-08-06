class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxf = max(freq.values())
        ties = sum(1 for v in freq.values() if v == maxf)
        a = len(tasks)
        b = (maxf -1)*(n + 1) + ties
        return max(a,b)