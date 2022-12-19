# https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        aux = 0
        self.n = [0]
        for i in nums:
            aux+=i
            self.n.append(aux)

    def sumRange(self, left: int, right: int) -> int:
        return self.n[right+1] - self.n[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)