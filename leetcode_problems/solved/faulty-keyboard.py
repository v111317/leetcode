#https://leetcode.com/problems/faulty-keyboard/description/

# Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string 
# that you have written. Typing other characters works as expected.
# You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
# Return the final string that will be present on your laptop screen.

class Solution:
    def finalString(self, s: str) -> str:
        if len(s)==1:
            return s
        
        l1 = []
        count = 0
        newStr = ""
        for i, letter in enumerate(s):
            if s[i] == "i":
                count += 1
                continue
                
            else:
                if count%2==1:
                    count = 0
                    while len(l1)!=0:
                        newStr += l1.pop()
                l1.append(letter)
        idx = 0        
        if count%2==1:
            idx = -1
        while len(l1)!=0:
            newStr += l1.pop(idx)
            
        return newStr
    
    def finalString2(self, s: str) -> str:
        if len(s)==1:
            return s
        
        l1 = []
        l2 = []
        hasStr = 1
        
        for letter in s:
            #print(letter, l1, l2)
            if letter == "i":
                if hasStr==1:
                    l2 = []
                    while len(l1)!=0:
                        l2.append(l1.pop())
                        hasStr = 2
                else:
                    l1 = []
                    while len(l2)!=0:
                        l1.append(l2.pop())
                        hasStr = 1
            else:
                if hasStr==1:
                    l1.append(letter)
                else:
                    l2.append(letter)        
        if hasStr==1:
            return "".join(l1)
        else:
            return "".join(l2)
        
sol1 = Solution()
print(sol1.finalString2("string"))
print(sol1.finalString2("poiinter"))
print(sol1.finalString2("goci"))
print(sol1.finalString2("viwif"))
print(sol1.finalString2("abiwmif"))
                

#time - 
#space - 
