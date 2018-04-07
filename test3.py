# counter = 100  # 整型变量
# miles = 1000.0  # 浮点型变量
# name = "runoob"  # 字符串
# title = 'python'
# print(counter)
# print(miles)
# print(name)
# print(title)

# a = b = c = 1
# print(a,b,c)

# a, b, c = 1, 2, "runoob"
# print(a,b,c)

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))

# a = 111
# print(isinstance(a,int))

# class A:
#     pass
# class B(A):
#     pass
# print(isinstance(A(), A))  # returns True
# print(type(A()) == A)      # returns True
# print(isinstance(B(), A))    # returns True
# print(type(B()) == A)        # returns False

# var1 = 1
# var2 = 10
# del var1,var2
# print(var1,var2) #报错

# print(5 + 4)  # 加法
# print(4.3 - 2) # 减法
# print(3 * 7)  # 乘法
# print(2 / 4)  # 除法，得到一个浮点数
# print(2 // 4) # 除法，得到一个整数
# print(17 % 3) # 取余
# print(2 ** 5) # 乘方

# str = 'Runoob'
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串

# print('Ru\noob')
# print(r'Ru\noob')

# word = 'Python'
# print(word[0], word[5])
# print(word[-1], word[-6])
#与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(tinylist * 2)  # 输出两次列表
# print(list + tinylist)  # 连接列表

# a = [1, 2, 3, 4, 5, 6]
# a[0] = 9
# a[2:5] = [13, 14, 15]
# print(a)
# a[2:5] = []   # 将对应的元素值设置为 []
# print(a)

# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
# print(tuple[2:])  # 输出从第三个元素开始的所有元素
# print(tinytuple * 2)  # 输出两次元组
# print(tuple + tinytuple)  # 连接元组

# tup = (1, 2, 3, 4, 5, 6)
# print(tup[0])
# print(tup[1:5])
# tup[0] = 11 #非法
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号
# print(tup1,tup2)

# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(Runoob=1, Google=2, Taobao=3))

# int(x [,base])
# 将x转换为一个整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串





