#https://leetcode.com/problems/gas-station/description/

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
# the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, 
# it is guaranteed to be unique
from typing import List

class Solution:
    #time limit exceeded
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas)==1:
            if gas[0]>=cost[0]:
                return 0
            else:
                return -1
            
        for i in range(len(gas)):
            if gas[i] > cost[i]:
                start = i
                gasTotal = 0
                costTotal = 0
                j = start
                count = len(gas)
                #print(start)
                while count>0:
                    j = j % len(gas)
                    gasTotal += gas[j]
                    costTotal += cost[j]
                    #print(gasTotal, costTotal)
                    if gasTotal < costTotal:
                        break
                    else:
                        count -= 1
                    j += 1
                if count==0:
                    return start
        
        return -1
    
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        result = 0
        net = 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            
            if net < 0:
                net = 0
                result = i+1
        
        return result
            

sol1 = Solution()
print(sol1.canCompleteCircuit2([1,2,3,4,5],[3,4,5,1,2]))
print(sol1.canCompleteCircuit2([2,3,4],[3,4,3]))
print(sol1.canCompleteCircuit2([1],[2]))
                    
                
                    