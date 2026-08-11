"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)         # ✓ sort by start
        return all(
            intervals[i].start >= intervals[i-1].end  # ✓ use .start / .end
            for i in range(1, len(intervals))
        )