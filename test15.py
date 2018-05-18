# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n, sum))

# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
# print("Good bye!")

# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")

# flag = 1
# while (flag): print('欢迎访问菜鸟教程!')
# print("Good bye!")

# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#      print (x)

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# for i in range(5):
#     print(i)
# for i in range(5,9) :
#     print(i)
# for i in range(0, 10, 3):
#     print(i)
# for i in range(-10, -100, -30):
#     print(i)
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])
# a = list(range(5))
# for i in range(len(a)):
#     print(a[i])

# for letter in 'Runoob':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
# print("Good bye!")

# for letter in 'Runoob':  # 第一个实例
#     if letter == 'o':  # 字母为 o 时跳过输出
#         continue
#     print('当前字母 :', letter)
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:  # 变量为 5 时跳过输出
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')

# while True:
#      pass  # 等待键盘中断 (Ctrl+C)
# class MyEmptyClass:
#      pass
# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
# print("Good bye!")

# for index, item in enumerate(sequence):
#     process(index, item)
# sequence = [12, 34, 34, 23, 45, 76, 89]
# for i, j in enumerate(sequence):
#     print(i, j)

# n = 0
# sum = 0
# for n in range(0,101):# n 范围 0-100
#     sum += n
# print(sum)

#外边一层循环控制行数
#i是行数
# i=1
# while i<=9:
#      #里面一层循环控制每一行中的列数
#      j=1
#      while j<=i:
#           mut =j*i
#           print("%d*%d=%d"%(j,i,mut), end="  ")
#           j+=1
#      print("")
#      i+=1

# for i in range(1,6):
#    for j in range(1, i+1):
#       print("*",end='')
#    print('\r')

# print(sum(range(101)))

# if a>1:
#     pass #如果没有内容，可以先写pass，但是如果不写pass，就会语法错误

#十进制转化
# while True:
#     number = input('请输入一个整数(输入Q退出程序)：')
#     if number in ['q','Q']:
#         break                #如果输入的是q或Q,结束退出
#     elif not number.isdigit():
#         print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
#         continue         #如果输入的数字不是十进制,结束循环,重新开始
#     else :
#             number = int(number)
#             print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
#             print('十进制 -->   八进制 ：%d -> 0o%o' %(number,number))
#             print('十进制 -->   二进制 ：%d ->'%number,bin(number))

def paixu(li) :
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])


