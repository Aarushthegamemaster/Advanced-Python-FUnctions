list1 = {1,2,3}
list2 = {4,5,6}
res = map(lambda x,y : x + y, list1, list2)
print("The additions of both of the lists is:")
print(list(res))

num1 = {1,2,3,4,5}
def sq(n):
    return n*n
square = list(map(sq,num1))
print("Square of numbers in list:")
print(square)