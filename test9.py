# list1 = ['Google', 'Runoob', 'Taobao']
# print (len(list1))
# list2=list(range(5)) # 创建一个 0-4 的列表
# print (len(list2))

# list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
# print ("list1 最大元素值 : ", max(list1))
# print ("list2 最大元素值 : ", max(list2))
# list1 = ['我', '爱', 'python']
# list2 = [100, 200, 300]
# print('list1的最大值:', max(list1))
# print('list2的最大值:', max(list2))
# print(id(list1[0]))
# print(id(list1[1]))
# print(id(list1[2]))
# print('我' > '爱')
# print('爱' > 'python')
# print('我' > 'python')

# list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
# print ("list1 最小元素值 : ", min(list1))
# print ("list2 最小元素值 : ", min(list2))

# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)
# str = "Hello World"
# list2 = list(str)
# print ("列表元素 : ", list2)

# list1 = ['Google', 'Runoob', 'Taobao']
# list1.append('Baidu')
# print ("更新后的列表 : ", list1)
# def changeextend(str):
#     "print string with extend"
#     mylist.extend([40,50,60]);
#     print ("print string mylist:",mylist)
#     return
# def changeappend(str):
#     "print string with append"
#     mylist.append( [7,8,9] )
#     print("print string mylist:",mylist )
#     return
# mylist = [10,20,30]
# changeextend( mylist );
# print ("print extend mylist:", mylist )
# changeappend( mylist );
# print ("print append mylist:", mylist )

# aList = [123, 'Google', 'Runoob', 'Taobao', 123];
# print ("123 元素个数 : ", aList.count(123))
# print ("Runoob 元素个数 : ", aList.count('Runoob'))

# list1 = ['Google', 'Runoob', 'Taobao']
# list2=list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print ("扩展后的列表：", list1)

# list1 = ['Google', 'Runoob', 'Taobao']
# print ('Runoob 索引值为', list1.index('Runoob'))
# print ('Taobao 索引值为', list1.index('Taobao'))

# list1 = ['Google', 'Runoob', 'Taobao']
# list1.insert(1, 'Baidu')
# print ('列表插入元素后为 : ', list1)

# list1 = ['Google', 'Runoob', 'Taobao']
# list1.pop()
# print ("列表现在为 : ", list1)
# list1.pop(0)
# print ("列表现在为 : ", list1)
# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(1)
# print ("删除的项为 :", list_pop)
# print ("列表现在为 : ", list1)

# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu', 'Ali', 'Baidu']
# list1.remove('Taobao')
# print ("列表现在为 : ", list1)
# list1.remove('Baidu')
# print ("列表现在为 : ", list1)

# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.reverse()
# print ("列表反转后: ", list1)

# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu', 'Ali']
# list1.sort()
# print ("列表排序后 : ", list1)
# list1 = ['我','爱','python']
# list2 = [100,200,300,400,300]
# list1.sort()
# list2.sort()
# print(list1,list2)

# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.clear()
# print ("列表清空后 : ", list1)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)
a=[0,1,2,3,4,5]
b=a
c=a.copy()
del a[1]
print(a)
print(b)
print(c)
b.remove(4)
print(a)
print(b)
print(c)
c.append(9)
print(a)
print(b)
print(c)