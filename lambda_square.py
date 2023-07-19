a1 = 3
b1 = lambda a1: a1 ** 2
print(b1(a1))


a = [1,2,3,4,5]
b = list(map(lambda a1: a1 ** 2,a))
print(b)

a = [1,2,4,5,6,7,8,9,10]
b = list(filter(lambda x: x%2== 0, a))
print(b)

from functools import reduce
product = reduce(lambda x,y: x + y, a)
print(product)

my_list = ['abcd', 'xyz', 'lmnopq']
m1 = [data.capitalize() for data in my_list]
print(m1)