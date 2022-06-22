class Solution:
    '''
    l3 is an empty list which will store the sorted values from l1 and l2.
    l is the total length of the two lists.
    even is a boolean variable that is True if l is even, False otherwise.
    The loop runs l/2 + 1 times, where it compares the first elements of l1 and l2 and appends the smaller value to l3. If one of the lists is empty, the loop appends the remaining values from the other list to l3. This way, l3 is sorted in ascending order.
    If l is odd, the function returns the last element of l3, which is the median.
    If l is even, the function returns the average of the last two elements of l3, which is the median.
    Complexity Analysis:

    Time complexity: The loop runs for l/2 + 1 times, where l is the length of the combined list, so the time complexity of the function is O(l).
    Space complexity: A new list l3 is created to store the sorted values, so the space complexity is O(l).
    '''
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
            l3 = []
            l = (len(l1) + len(l2))
            even = l%2 == 0
            for i in range(int(l/2) + 1):
                if(len(l1) == 0):
                    l3.append(l2.pop(0))
                elif(len(l2) == 0):
                    l3.append(l1.pop(0))
                else:
                    if(l1[0] < l2[0]):
                        l3.append(l1.pop(0))
                    else:
                        l3.append(l2.pop(0))
            if(not even):
                return l3[-1]
            else:
                 return (l3[-2] + l3[-1])/2