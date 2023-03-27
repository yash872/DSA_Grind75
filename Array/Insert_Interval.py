# Insert Interval
# https://leetcode.com/problems/insert-interval


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res =[]
        i=0
        for i, item in enumerate(intervals):
            if item[1] < newInterval[0]:
                res.append(item) 
            elif item[0] > newInterval[1]:
                i-=1
                break
            else:
                newInterval[0] = min(item[0],newInterval[0])
                newInterval[1] = max(item[1],newInterval[1])
             
        return res + [newInterval] +intervals[i+1:]