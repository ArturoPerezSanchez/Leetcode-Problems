# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        res = []
        for i in l:
            if(i == ".." and len(res) != 0):
                res.pop(-1)
            elif(i != "" and i != "." and i != ".."):
                res.append(i)
        if(not res):
            return "/"
        else:
            return '/' + '/'.join(res)