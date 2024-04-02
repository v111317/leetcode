#https://leetcode.com/problems/most-common-word/description/

# Given a string paragraph and a string array of the banned words banned, return the most frequent word 
# that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = []
        words = []
        punctuation = ["!", "?", ",", ";", ".", " ", "'"]
        for letter in paragraph:
            if letter in punctuation:
                if len(word)>0:
                    words.append("".join(word))
                    word = []
            else:
                word.append(letter)
        if len(word)>0:
            words.append("".join(word))

        words = [word.lower() for word in words]
        
        wordMap = {}
        maxCount = -1
        mostFrequent = ""
        for i, word in enumerate(words):
            if words[i] not in banned:
                if words[i] in wordMap:
                    wordMap[words[i]] += 1
                    if wordMap[words[i]] > maxCount:
                        maxCount = wordMap[words[i]]
                        mostFrequent = words[i]
                else:
                    wordMap[words[i]] = 1
                    if maxCount==-1:
                        maxCount = 1
                        mostFrequent = words[i]
        return mostFrequent
        
sol1 = Solution()
# print(sol1.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
# print(sol1.mostCommonWord("a, a, a, a, b,b,b,c, c", ["hit"]))
# print(sol1.mostCommonWord("a.", []))
# print(sol1.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
#print(sol1.mostCommonWord("Bob", []))
para = "j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?"
banned = ["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"]
print(sol1.mostCommonWord(para, banned))


