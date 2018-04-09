# str = "this is string example from runoob....wow!!!"
# print ("str.capitalize() : ", str.capitalize())
# 1、首字符会转换成大写，其余字符会转换成小写。
# 2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。

# str = "[www.runoob.com]"
# print ("str.center(40, '*') : ", str.center(40, '*'))
# 1、如果 width 小于字符串宽度直接返回字符串，不会截断
# 2、fillchar 默认是空格
# 3、fillchar 只能是单个字符

# str="www.runoob.com"
# sub='o'
# print ("str.count('o') : ", str.count(sub))
# sub='w'
# print ("str.count('w', 0, 2) : ", str.count(sub,0,2))
# sub='run'
# print ("str.count('run', 0, 10) : ", str.count(sub,0,10))

# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
# print(str)
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
# print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
# print("GBK 解码：", str_gbk.decode('GBK','strict'))

# Str='Runoob example....wow!!!'
# suffix='!!'
# print (Str.endswith(suffix))
# print (Str.endswith(suffix,20))
# suffix='run'
# print (Str.endswith(suffix))
# print (Str.endswith(suffix, 0, 19))

# str = "this is\tstring example....wow!!!"
# print ("原始字符串: " + str)
# print ("替换 \\t 符号: " + str.expandtabs())
# print ("使用16个空格替换 \\t 符号: " + str.expandtabs(16))
# \t 是补全当前字符串长度到8的整数倍，最少 1 个最多 8 个空格。
# 补多少要看你 \t 前字符串长度。
# 比如当前字符串长度 8，那么 \t 后长度是 16，也就是补 8 个空格。
# 如果当前字符串长度 12，此时 \t 后长度是 16，补 4 个空格。
# str1 = "this is\tstring example....wow!!!"
# str2 = "athis is\tstring example....wow!!!"
# str3 = "athis is        string example....wow!!!"  # is 和 string 中间输入 8 个空格
# print(str1)
# print("a"+str1)
# print(str2)
# print(str3)

# str1 = "Runoob example....wow!!!"
# str2 = "exam";
# print(str1.find(str2))
# print(str1.find(str2, 5))
# print(str1.find(str2, 10))
# info = 'abca'
# print(info.find('a'))      # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
# print(info.find('a', 1))   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
# print(info.find('3'))      # 查找不到返回-1

# str1 = "Runoob example....wow!!!"
# str2 = "exam";
# print (str1.index(str2))
# print (str1.index(str2, 5))
# print (str1.index(str2, 10))

# str = "runoob2016"  # 字符串没有空格
# print(str.isalnum())
# str = "www.runoob.com"
# print(str.isalnum())

# str = "runoob"
# print (str.isalpha())
# str = "Runoob example....wow!!!"
# print (str.isalpha())

# str = "123456";
# print (str.isdigit())
# str = "Runoob example....wow!!!"
# print (str.isdigit())

# str = "RUNOOB example....wow!!!"
# print (str.islower())
# str = "runoob example....wow!!!"
# print (str.islower())

# str = "runoob2016"
# print (str.isnumeric())
# str = "23443434"
# print (str.isnumeric())
# s.isdigit、isdecimal 和 s.isnumeric 区别：
# isdigit()
# True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
# False: 汉字数字
# Error: 无
# isdecimal()
# True: Unicode数字，，全角数字（双字节）
# False: 罗马数字，汉字数字
# Error: byte数字（单字节）
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 无
# Error: byte数字（单字节）
# num = "1"  #unicode
# num.isdigit()   # True
# num.isdecimal() # True
# num.isnumeric() # True
# num = "1" # 全角
# num.isdigit()   # True
# num.isdecimal() # True
# num.isnumeric() # True
# num = b"1" # byte
# num.isdigit()   # True
# num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
# num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'
# num = "IV" # 罗马数字
# num.isdigit()   # True
# num.isdecimal() # False
# num.isnumeric() # True
# num = "四" # 汉字
# num.isdigit()   # False
# num.isdecimal() # False
# num.isnumeric() # True

# str = "       "
# print (str.isspace())
# str = "Runoob example....wow!!!"
# print (str.isspace())
# 空白符包含：空格、制表符(\t)、换行(\n)、回车等(\r）
# print (' \t\r\n'.isspace())
# print ('\0'.isspace())
# print (' a '.isspace())

# str = "This Is String Example...Wow!!!"
# print (str.istitle())
# str = "This is string example....wow!!!"
# print (str.istitle())

# str = "THIS IS STRING EXAMPLE....WOW!!!"
# print (str.isupper())
# str = "THIS is string example....wow!!!"
# print (str.isupper())

# s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# print (s1.join( seq ))
# print (s2.join( seq ))
# str.join(sequence) 函数中的 sequence 中的元素必须是字符串，否则会报错
# jn1="-"
# jn2="------"
# str='name'
# print(jn1.join(str))    #字符串也属于序列
# print(jn2.join(str))    #使用多字符连接序列
# fruits={'apple','banana'}
# print(jn1.join(fruits))   #连接的序列是集合
# animals=("pig","dog")
# print(jn1.join(animals))   #连接的序列是元祖
# students={"name1":"joy","name2":"john","name3":"jerry"}   #连接的序列是字典，会将所有key连接起来
# print(jn1.join(students))

# str = "runoob"
# print(len(str))             # 字符串长度
# l = [1,2,3,4,5]
# print(len(l))               # 列表元素个数

# str = "Runoob example....wow!!!"
# print (str.ljust(50, '*'))

# str = "Runoob EXAMPLE....WOW!!!"
# print(str.lower())

# str = "     this is string example....wow!!!     ";
# print( str.lstrip() );
# str = "88888888this is string example....wow!!!8888888";
# print( str.lstrip('8') );

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
# str = "this is string example....wow!!!"
# print (str.translate(trantab))

# str = "runoob"
# print ("最大字符: " + max(str))
# str = "runoob";
# print ("最小字符: " + min(str));

# str = "www.w3cschool.cc"
# print ("菜鸟教程旧地址：", str)
# print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
# str = "this is string example....wow!!!"
# print (str.replace("is", "was", 1))

# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print (str1.rfind(str2))
# print (str1.rfind(str2, 0, 10))
# print (str1.rfind(str2, 10, 0))
# print (str1.find(str2))
# print (str1.find(str2, 0, 10))
# print (str1.find(str2, 10, 0))

# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print (str1.rindex(str2))
# print (str1.rindex(str2,10))

# str = "this is string example....wow!!!"
# print (str.rjust(50, '*'))
#
# str = "     this is string example....wow!!!     "
# print (str.rstrip())
# str = "*****this is string example....wow!!!*****"
# print (str.rstrip('*'))

# str = "this is string example....wow!!!"
# print (str.split( ))
# print (str.split('i',1))
# print (str.split('w'))

# print('ab c\n\nde fg\rkl\r\n'.splitlines())
# print('ab c\n\nde fg\rkl\r\n'.splitlines(True))

# str = "this is string example....wow!!!"
# print (str.startswith( 'this' ))
# print (str.startswith( 'string', 8 ))
# print (str.startswith( 'this', 2, 4 ))

# str = "*****this is string example....wow!!!*****"
# print (str.strip( '*' ))

# str = "this is string example....wow!!!"
# print (str.swapcase())
# str = "This Is String Example....WOW!!!"
# print (str.swapcase())

# str = "this is string example from runoob....wow!!!"
# print (str.title())

# 制作翻译表
# bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
# print(b'runoob'.translate(bytes_tabtrans, b'o'))

# str = "this is string example from runoob....wow!!!";
# print ("str.upper() : ", str.upper())

# str = "this is string example from runoob....wow!!!"
# print ("str.zfill : ",str.zfill(40))
# print ("str.zfill : ",str.zfill(50))

str = "runoob2016"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())