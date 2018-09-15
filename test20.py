# s = 'Hello, Runoob'
# print(str(s))
# print(repr(s))
# print(str(1/7))
# x = 10*3.25
# y = 200*200
# s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
# print(s)
# #  repr() 函数可以转义字符串中的特殊字符
# hello = 'hello, runoob\n'
# hello2 = repr(hello)
# print(hello)
# print(hello2)
# # repr() 的参数可以是 Python 的任何对象
# print(repr((x, y, ('Google', 'Runoob'))))

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     # 注意前一行 'end' 的使用
#     print(repr(x * x * x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))

# str.format() 的基本使用如下:
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。

# print('{0} 和 {1}'.format('Google', 'Runoob'))
# print('{1} 和 {0}'.format('Google', 'Runoob'))

# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',other='Taobao'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# import math
# print('常量 PI 的值近似为： {}。'.format(math.pi))
# print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
# import math
# print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# import math
# print('常量 PI 的值近似为：%5.3f。' % math.pi)

# str = input("请输入：");
# print ("你输入的内容是: ", str)

# str = float(input("请输入："))*float(input("请输入："))
# print("输入的内容是:",str)

# open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
# 模式	       r	r+	w	w+	a	a+
# 读	       +	+		+		+
# 写		        +	+	+	+	+
# 创建			        +	+	+	+
# 覆盖			        +	+
# 指针在开始	+	+	+	+
# 指针在结尾					+	+

# f = open("/foo.txt", "w")
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# f.close()

# f = open("/foo.txt", "r")
# str = f.read()
# print(str)
# f.close()

# f = open("/foo.txt", "r")
# str = f.readline()
# str2 = f.readline()
# print(str)
# print(str2)
# f.close()

# f = open("/foo.txt","r")
# str = f.readlines()
# # 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
# # str = f.readlines(20)
# print(str)
# f.close()

# f = open("/foo.txt", "r")
# for line in f:
#     print(line, end='')
# f.close()

# f = open("/foo.txt", "w")
# num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# print(num)
# f.close()

# f = open("/foo1.txt", "w")
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
# f.close()

# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# f = open("/foo.txt", "r")
# str = f.tell()
# print(str)
# f.close()

# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
# from_what 值为默认为0，即文件开头。下面给出一个完整的例子：

# f = open('/foo2.txt','w')
# f.close()
# f2 = open('/foo2.txt', 'rb+')
# s = f2.write(b'0123456789abcdef')
# print(s)
# print(f2.seek(5))
# print(f2.read(1))
# print(f2.seek(-3, 2))
# print(f2.read(1))
# f2.close()

# with open('/foo2.txt', 'r') as f:
#     read_data = f.read()
# print(read_data)
# f.close()

# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本接口：
# pickle.dump(obj, file, [,protocol])
# 有了 pickle 这个对象, 就能对 file 以读取的形式打开:
# x = pickle.load(file)

# import pickle
# # 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
# output = open('data.pkl', 'wb')
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
# output.close()

# import pprint, pickle
# #使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
# pkl_file.close()

# # python文件写入也可以进行网站爬虫
# from urllib import request
# response = request.urlopen("http://www.baidu.com/")  # 打开网站
# fi = open("project.txt", 'w')                        # open一个txt文件
# page = fi.write(str(response.read()))                 # 网站代码写入
# print(page)
# fi.close()                                           # 关闭txt文件

# print('%o' % 20) # 八进制24
# print('%d' % 20) # 十进制20
# print('%x' % 24) # 十六进制18

# print('%f' % 1.11)         # 默认保留6位小数1.110000
# print('%.1f' % 1.11)       # 取1位小数1.1
# print('%e' % 1.11)         # 默认6位小数，用科学计数法1.110000e+00
# print('%.3e' % 1.11)       # 取3位小数，用科学计数法1.110e+00
# print('%g' % 1111.1111)    # 默认6位有效数字1111.11
# print('%.7g' % 1111.1111)  # 取7位有效数字1111.111
# print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法1.1e+03

# print('%s' % 'hello world')       # 字符串输出hello world
# print('%20s' % 'hello world')     # 右对齐，取20位，不够则补位         hello world
# print('%-20s' % 'hello world')    # 左对齐，取20位，不够则补位hello world
# print('%.2s' % 'hello world')     # 取2位he
# print('%10.2s' % 'hello world')   # 右对齐，取2位        he
# print('%-10.2s' % 'hello world')  # 左对齐，取2位he

# 将 mode 设置为 w+ 或 a+ 时，发现直接进行读操作，得到的内容都是空，但原因不太相同：
# 如果 mode 设置为 w+，即使没有执行 write 操作，也会将文件内容清空，因此这个时候直接进行读草稿，读到的是空内容。
# f = open("E:\\administrator\\Desktop\\test.txt", "w+")
# 如果 mode 设置为 a+，文件指针位置默认在最后面，因为读内容时，是按照指针的位置往后读，所以如果指针位置在最后，那读出来的是空，在读之前，一定要注意确认好指针位置是对的。
# f = open("E:\\administrator\\Desktop\\test.txt", "a+")
# f.write("append content")
# print(f.tell())  #此时指针在文件字符末尾处
# f.seek(0)
# print(f.tell())  # 指针回到0的位置
# str = f.read()
# print(str)
# f.close()

# 通过pickle序列化实现一个简单联系人信息管理：
import pickle
import os

datafile = 'person.data'
line = '======================================='
message = '''
=======================================
Welcome bookmark:
    press 1 to show list
    press 2 to add pepole
    press 3 to edit pepole
    press 4 to delete pepole
    press 5 to search pepole
    press 6 to show menu
    press 0 to quit
=======================================
'''
print(message)


class Person(object):
    """通讯录联系人"""

    def __init__(self, name, number):
        self.name = name
        self.number = number


# 获取数据
def get_data(filename=datafile):
    # 文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None


# 写入数据
def set_data(name, number, filename=datafile):
    personList = {} if get_data() == None else get_data()

    with open(filename, 'wb') as f:
        personList[name] = Person(name, number)
        pickle.dump(personList, f)


# 保存字典格式的数据到文件
def save_data(dictPerson, filename=datafile):
    with open(filename, 'wb') as f:
        pickle.dump(dictPerson, f)


# 显示所有联系人
def show_all():
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name, v.number)
        print(line)
    else:
        print('not yet person,please add person')
        print(line)


# 添加联系人
def add_person(name, number):
    set_data(name, number)
    print('success add person')
    print(line)


# 编辑联系人
def edit_person(name, number):
    personList = get_data()
    if personList:
        personList[name] = Person(name, number)
        save_data(personList)
        print('success edit person')
        print(line)


# 删除联系人
def delete_person(name):
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)
            print('success delete person')
        else:
            print(name, ' is not exists in dict')
        print(line)


# 搜索联系人
def search_person(name):
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(name).number)
        else:
            print('No this person of ', name)
        print(line)


while True:
    num = input('>>')

    if num == '1':
        print('show all personList:')
        show_all()
    elif num == '2':
        print('add person:')
        name = input('input name>>')
        number = input('input number>>')
        add_person(name, number)
    elif num == '3':
        print('edit person:')
        name = input('input name>>')
        number = input('input number>>')
        edit_person(name, number)
    elif num == '4':
        print('delete person:')
        name = input('input name>>')
        delete_person(name)
    elif num == '5':
        print('search :')
        name = input('input name>>')
        search_person(name)
    elif num == '6':
        print(message)
    elif num == '0':
        break
    else:
        print('input error, please retry')