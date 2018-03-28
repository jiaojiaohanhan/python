# word = '字符串'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落，
# 可以由多行组成"""
# print(word)
# print(sentence)
# print(paragraph)

# str='Runoob'
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始的后的所有字符
# print(str * 2)             # 输出字符串两次
# print(str + '你好')        # 连接字符串
# print('------------------------------')
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# a=2
# if a==1 :
#     print(1)
# elif a==2 :
#     print(2)
# else :
#     print(0)

# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )

# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# # print(sys.argv)
# print ('\n python 路径为',sys.path)

# from sys import argv, path  # 导入特定的成员
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
# print('argv:', argv)

help(max) #调用 python 的 help() 函数可以打印输出一个函数的文档字符串
#如果仅仅想得到文档字符串
print(max.__doc__) #注意，doc的前后分别是两个下划线

