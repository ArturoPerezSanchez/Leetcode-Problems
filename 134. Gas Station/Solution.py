# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif_list = [0]*len(gas)
        lowest_position_index = 0
        lowest_position_value = gas[0] - cost[0]
        for i in range(len(gas)):
            curr_position = dif_list[i-1] + gas[i] - cost[i]
            dif_list[i] = curr_position
            if (curr_position < lowest_position_value):
                lowest_position_value = curr_position
                lowest_position_index = i
        print(dif_list)
        if(dif_list[-1] < 0): return -1
        return (lowest_position_index+1)%(len(gas))