# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b

# i = 256*256
# print('i 的值为：', i)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b

# a=10;b=388;c=98
# print(a,b,c,sep='@')

# def fab(n):
#     if n<1:
#         print('输入有误！')
#         return -1
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# print(fab(10))

# n=int(input('请输入一个整数:'))
# def fab(n):
#     if n<1:
#         print('输入有误！')
#         return -1
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# result=[]
# for i in range(1,n+1):
#     result.append(fab(i))
# print(result)

n=int(input('请输入一个整数:'))
dic = {0:0,1:1}
def fib(n):
    if n in dic:
        return dic[n]
    else:
        temp = fib(n-1)+fib(n-2)
        dic[n] = temp
        return temp
for i in range(n):
    print(fib(i),end=" ")

