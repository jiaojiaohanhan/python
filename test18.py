# a = [66.25, 333, 333, 1, 1234.5,'x']
# print(a.count(333), a.count(66.25), a.count('x'))
# a.insert(2,-1)
# a.append(333)
# print(a)
# print(a.index(333))
# a.remove(333)
# print(a)
# a.reverse()
# print(a)
# a.remove('x')
# a.sort()
# print(a)
# b=['aa','bb']
# a.extend(b)
# print(a)
# print(a.pop(6))
# c=a.copy()
# print(c)

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# print(queue)
# queue.append("Terry")
# queue.append("Graham")
# queue.appendleft("Tom")
# queue.appendleft("Haylr")
# print(queue.popleft())
# print(queue.popleft())
# print(queue.pop())
# print(queue.pop())
# print(queue)

# vec=[2,4,6]
# print([3*x for x in vec])
# print([[x,x*2]for x in vec])
# print([3*x for x in vec if x>3])
# print([[x,x*2]for x in vec if x>3])

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])

# vec1=[2,4,6]
# vec2=[4,3,-9]
# print([x*y for x in vec1 for y in vec2])
# print([x+y for x in vec1 for y in vec2])
# print([vec1[i]*vec2[i] for i in range(len(vec1))])

# print([str(round(355/113,i)) for i in range(1,6)])

# from numpy import *
# import numpy as np
# ma = matrix([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
# ma = np.mat([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
# print(ma)

# matrix = [[1,2,3,4],[5,6,7,8],[10,11,12,13]]
# print(matrix)
# print([[row[i] for row in matrix] for i in range(4)])
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)
# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# a = "gaoxing"
# del a
# print(a)

# t = 12345, 54321, 'hello!'
# print(t[0])
# print(t)
# u = t,(1,2,3,4,5)
# print(u)
# m = t,132,'bb'
# print(m)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)
# print('crabgrass' in basket)

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# # 在 a 中的字母，但不在 b 中
# print(a-b)
# # 在 a 或 b 中的字母
# print(a|b)
# # 在 a 和 b 中都有的字母
# print(a&b)
# # 在 a 或 b 中的字母，但不同时在 a 和 b 中
# print(a^b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(list(tel.keys()))
# print(sorted(tel.keys()))
# print('guido' in tel)
# print('jack' not in tel)

# dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dict1)
# dict2 = {x: x**2 for x in (2, 4, 6)}
# print(dict2)
# dict3 = dict(sape=4139, guido=4127, jack=4098)
# print(dict3)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(set(basket)):
#     print(i)

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]
# t = a,b,c
# print(t)
# del b[1:4]
# print(t)

# [x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
# 他的执行顺序是:
# for x in range(1,5):
#     if x > 2:
#         for y in range(1,4):
#             if y < 3:
#                 x*y

questions=['name','quest','favorite color']
answers=['qinshihuang','the holy','blue']
for q,a in zip(questions,answers):
    print('what is your %s? it is %s' %(q,a))
    print('what is your {0}? it is {1}'.format(q,a))
