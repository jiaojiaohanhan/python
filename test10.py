# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5 )
# tup3 = "a", "b", "c", "d"  #  不需要括号也可以
# print(type(tup3))

# tup1 = ()
# tup1 = (50)
# print(type(tup1))     # 不加逗号，类型为整型
# tup1 = (50,)
# print(type(tup1))     # 加上逗号，类型为元组

# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])

# tup1 = (12, 34.56);
# tup2 = ('abc', 'xyz')
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
# # 创建一个新的元组
# tup3 = tup1 + tup2;
# print (tup3)

# tup = ('Google', 'Runoob', 1997, 2000)
# print (tup)
# del tup;
# print ("删除后的元组 tup : ")
# print (tup)

# L = ('Google', 'Taobao', 'Runoob')
# print(L[2])
# print(L[-2])
# print(L[1:])

# tuple1 = ('Google', 'Runoob', 'Taobao')
# print(len(tuple1))
# tuple2 = ('5', '4', '8')
# print(max(tuple2))
# tuple2 = ('5', '4', '8')
# print(min(tuple2))
# list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# tuple1=tuple(list1)
# print(tuple1)

import collections
#two ways to define the field name for namedtuple
#User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', 'name age id')
user = User('tester', '22', '464643123')
print(user)