#https://leetcode.com/problems/number-of-recent-calls/description/
    
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
# and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

class RecentCounter:

    def __init__(self):
        self.timeList = []
        
    def findIdxTime(self, startTime):
        if startTime < 0 :
            return 0
        
        start = 0
        end = len(self.timeList) - 1
        
        while start <= end:
            mid = (start+end)//2
            print(" => ", start, mid, end)
            print(" --> ", startTime)
            
            if self.timeList[mid]==startTime:
                return mid
            
            if startTime < self.timeList[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return mid        

    def ping(self, t: int) -> int:
        self.timeList.append(t)
        startTime = t - 3000
        for i in range(len(self.timeList)):
            if self.timeList[i]>=startTime:
                break    
        return len(self.timeList) - i
        

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))