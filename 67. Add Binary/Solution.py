# https://leetcode.com/problems/add-binary

class Solution(object):
    def addBinary(self, a, b):
        return bin(int(b,2)+int(a,2))[2:]