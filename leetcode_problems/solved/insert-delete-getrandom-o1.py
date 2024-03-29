#https://leetcode.com/problems/insert-delete-getrandom-o1/description/

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. 
# Returns true if the item was not present, false otherwise.

# bool remove(int val) Removes an item val from the set if present. 
# Returns true if the item was present, false otherwise.

# int getRandom() Returns a random element from the current set of elements 
# (it's guaranteed that at least one element exists when this method is called). 
#  Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
import random

class RandomizedSet:

    def __init__(self):
        self.numSet = []

    def insert(self, val: int) -> bool:
        if val not in self.numSet:
            self.numSet.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.numSet:
            self.numSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.numSet)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())

#time - O(1)
#space - O(1)