
def square_num(n):
    return n*n

square_num2 = lambda n: n*n

#print(square_num2(4))
#print(square_num(5))

list1 = [1,2,3,4,5]

list2 = map(lambda x: x*10, list1)
print(list(list2))

list3 = ["amruds", "apple", "orange", "melon"]

list3.sort(key=lambda item: len(item))
print(list3)

list3.sort(key=len)