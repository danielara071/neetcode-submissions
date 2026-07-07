"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import itemgetter

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        if not intervals:
            return True
        prev = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = intervals[i].end
        return True