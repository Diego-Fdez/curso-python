from functools import reduce

number_list = [1,2,3,4,5,6,7,8,9,10]

odd_list = list(filter(lambda x: x % 2, number_list))

reduce_list = reduce(lambda x,y: x + y, odd_list)
print(reduce_list)