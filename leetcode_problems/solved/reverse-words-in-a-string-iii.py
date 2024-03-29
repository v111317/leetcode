#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

#Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        result = []
        for word in words:
            arr = list(word)
            strLen = len(arr)
            i = 0
            while i < strLen//2:
                temp = arr[i]
                arr[i] = arr[strLen-1-i]
                arr[strLen-1-i] = temp
                i += 1
            result.append("".join(arr))
        return " ".join(result)

sol1 = Solution()
print(sol1.reverseWords("Let's take LeetCode contest"))

#time - O(n)
#space - O(n)