# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
# function to check    
        def check(s1, words_cnt):
            j = 0   # two pointers: i and j
            for i in range(ls_w,len(s1)+1,ls_w):
                if s1[j:i] in words_cnt:
                    words_cnt[s1[j:i]] -= 1
                    j = i

            return all(x==0 for x in words_cnt.values())

        # main part
        words_cnt = collections.defaultdict(int)

        ls = 0 # total s length
        ls_w = len(words[0]) #single word length

        for word in words:
            words_cnt[word] += 1
            ls += len(word)

        ans = []
        for i in range(0,len(s)-ls+1):
            if check(s[i:i+ls], words_cnt.copy()):
               ans.append(i)

        return ans
            