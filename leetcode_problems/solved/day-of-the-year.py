#https://leetcode.com/problems/day-of-the-year/description/

#Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

class Solution:
    def dayOfYear(self, date: str) -> int:
        [year, month, day] = date.split("-")
        monthArr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(year)
        month = int(month)
        day = int(day)
        count = day
        for i in range(1, month):
            count += monthArr[i]
        
        if month>2:
            if year%100 ==0:
                if year%400==0:
                    count += 1
            else:
                if year%4==0:
                    count += 1
        return count
    
sol1 = Solution()
print(sol1.dayOfYear("2019-10-01"))
print(sol1.dayOfYear("2019-01-09"))
print(sol1.dayOfYear("2019-02-10"))
print(sol1.dayOfYear("2012-01-02"))


#time - O(1)
#space - O(1)
        
