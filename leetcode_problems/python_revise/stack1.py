#https://www.geeksforgeeks.org/stack-in-python/

#issue with memory if stack grows
#O(n)
class MyStack:
    
    def __init__(self):
        self.store = []
        
    def push(self, num):
        self.store.append(num)
        
    def pop(self):
        numElements = len(self.store)
        
        if numElements==0:
            return None
        else:
            return self.store.pop(numElements-1)
    
    def print(self):
        for i in range(len(self.store)-1, -1, -1):
            print(self.store[i])
    

# s1 = MyStack()
# s1.push(10)
# s1.push(3)
# s1.print()

# n = s1.pop()
# s1.print()


#has O(1) for append and pop
from collections import deque

stack2 = deque()

stack2.append(10)
stack2.append(5)
stack2.append(100)
stack2.append(20)
print(stack2)

print(stack2.pop()) 
print(stack2)

from queue import LifoQueue

