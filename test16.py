# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# import sys  # 引入 sys 模块
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# import sys
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# import sys
# def fibonacci(n,w=0): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         print('%d,%d' % (a,b))
#         counter += 1
# f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()
# import sys
# def fibonacci(n,w=0): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         #yield a
#         a, b = b, a + b
#         print('%d,%d' % (a,b))
#         counter += 1
# f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()
# l = [i for i in range(0,15)]
# print(l)
# m = (i for i in range(0,15))
# print(m)
# for g in m:
#     print(g,end=', ')#m即是迭代器

# import sys
# def fab(max):
#    n, a, b = 0, 0, 1
#    L = []
#    while n < max:
#        L.append(b)
#        a, b = b, a + b
#        n = n + 1
#    return L
# #上面那个 fab 函数从参数 max 返回一个有 max 个元素的 list，当这个 max 很大的时候，会非常的占用内存。
# f = iter(fab(1000))
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# #这样我们实际上是先生成了一个 1000 个元素的 list:f，然后我们再去使用这个 f。

#因为我们实际使用的是 list 的遍历，也就是 list 的迭代器。那么我们可以让这个函数 fab 每次只返回一个迭代器——一个计算结果，而不是一个完整的 list：
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print b
#         a, b = b, a + b
#         n = n + 1
#这样，我们每次调用fab函数，比如这样：
# for x in fab(10):
#     print(x)
#或者 next 函数之类的，实际上的运行方式是每次的调用都在 yield 处中断并返回一个结果，然后再次调用的时候再恢复中断继续运行。
# f = fab(10)
# for i in range(10):
#     print(next(f))

def get():
    m = 0
    n = 2
    l = ['s', 1, 3]
    k = {1: 1, 2: 2}
    p = ('2', 's', 't')
    while True:
        m += 1
        yield m
        yield m, n, l, k, p
it = get()
print(next(it))  # 1
print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))
print(next(it))  # 2
print(type(next(it)))  # <class 'tuple'>
print(type(next(it)))  #<class 'int'>
#返回值的类型，应该是当前调用时，yield 返回值的类型。
