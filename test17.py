# def hello():
#     print("hello world")
# hello()

# def area(width,height):
#     return width*height
# def welcome(name):
#     print("Welcome",name)
# welcome("wang")
# w = 5
# h = 4
# print(area(w,h))

# a=[1,2,3]
# a="Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
# 可以是指向 List 类型对象，也可以是指向 String 类型对象

# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

# def ChangeInt(a):
#     a = 10
# b = 2
# ChangeInt(b)
# print(b)  # 结果是 2

# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1,2,3,4])
#     print("函数内取值: ", mylist)
#     return
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)

# 可写函数说明
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="runoob")

# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ",arg1,vartuple)
#     # print(arg1)
#     # print(vartuple)
# # 调用printinfo 函数
# printinfo(70, 60, 50)

# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)

# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

# 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入
# def f(a,b,*,c):
#     return a+b+c
# # print(f(1,2,3))
# print(f(1,2,c=3))

# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

# # 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))

# 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print("函数内 : ", total)
#     return total
# # 调用sum函数
# total = sum(10, 20)
# print("函数外 : ", total)

# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
# x = int(2.9)  # 内建作用域
# g_count = 0  # 全局作用域
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
# if True:
#     msg = "I Love World"
# print(msg)
# 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问
# def test():
#     msg_inner = "I am a student"
# print(msg_inner)

# total = 0  # 这是一个全局变量
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2  # total在这里是局部变量.
#     print("函数内是局部变量 : ", total)
#     return total
# # 调用sum函数
# sum(10, 20)
# print("函数外是全局变量 : ", total)

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

# a = 10
# def test(a):
#     a = a + 1
#     print(a)
# test(a)

# 可写函数说明
# def printinfo(age=35,name):   # 默认参数不在最后，会报错
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return

# 把N个关键字参数转化为字典:
# def func(country,province,**kwargs):
#     print(country,province,kwargs)
# func("China","Sichuan",city = "Chengdu", section = "JingJiang")

# g= lambda x,y : x**2+y**2
# print(g(2,3))
# print(g(y=3,x=2))

# g= lambda x=0,y=0 : x**2+y**2
# print(g(2,3))
# print(g(2))
# print(g(y=3))

# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist = [1, 2, 3, 4]
#     print("函数内取值: ", mylist)
#     return
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)

# 内置作用域是通过一个名为builtin的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
# 在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
import builtins
print(dir(builtins))

# 函数也可以以一个函数为其参数:
def hello():
  print ("Hello, world!")
def execute(f):
  "执行一个没有参数的函数"
  f()
execute(hello)

# 可以通过 函数名.__doc__ 的方式来显示函数的说明文档，
# 感觉这个如果在阅读比较大的程序时应该会有用，同时也在提示自己在写函数时注意添加文档说明
def add(a,b):
    "这是 add 函数文档"
    return a+b
print (add.__doc__)

# 不同于 C 语言，Python 函数可以返回多个值，多个值以元组的方式返回:
def fun(a,b):
    "返回多个值，结果以元组形式表示"
    return a,b,a+b
print(fun(1,2))

# 在不改变当前函数的情况下, 给其增加新的功能:
def log(pr):#将被装饰函数传入
    def wrapper():
        print("**********")
        return pr()#执行被装饰的函数
    return wrapper#将装饰完之后的函数返回（返回的是函数名）
@log
def pr():
    print("我是居民")
pr()