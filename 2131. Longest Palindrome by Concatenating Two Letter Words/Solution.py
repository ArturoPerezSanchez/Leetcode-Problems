# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        extra = 0
        res = 0
        d = Counter(words)
        # for word in words: d[word] = d.get(word, 0) + 1
        for word in d:
            if(word[0] == word[1]):
                res += (d[word]//2)*4
                if(not extra and d[word]%2 == 1): extra = 2
            else:
                rev = word[1] + word[0]
                if(rev in d):
                    res += min(d[rev], d[word])*2
        return res + extra
    
    # Ineficient solution O(n^2)
    def longestPalindrome2(self, words: List[str]) -> int:
        extra = 0
        res = 0
        for i in range(len(words)):
            if(words[i] == None): continue
            word = words[i][1] + words[i][0]
            for j in range(i+1,len(words)):
                if (words[j] == word):
                    words[j] = None
                    res +=4
                    break
            else:
                if(not extra and word[0] == word[1]):
                    extra = 2
        return res + extra