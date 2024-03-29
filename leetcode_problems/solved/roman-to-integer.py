class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = s
        
        romanToNumMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        subMap = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        addList = []
        
        for letterPair in subMap:
            if letterPair in romanNum:
                addList.append(subMap[letterPair])
                idx = romanNum.index(letterPair)
                if idx == 0:
                    romanNum = romanNum[2:len(romanNum)+1]
                else:
                    romanNum = romanNum[0:idx] + romanNum[idx+2:len(romanNum)+1]
                
        for letter in romanToNumMap:
            if letter in romanNum:
                count = romanNum.count(letter)
                addList += [romanToNumMap[letter] for i in range(0, count)]
                idx = romanNum.index(letter)
              
        return sum(addList)
    
    def romanToInt2(self, s: str) -> int:
        
        romanToNumMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        
        #romanNum = s
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        num = 0
        
        for letter in s:
            num += romanToNumMap[letter]
            
        return num
        
    
            
sol1 = Solution()
#print(sol1.romanToInt2("MCMXCIV"))
print(sol1.romanToInt2("VIII"))