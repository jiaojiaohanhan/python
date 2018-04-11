# dict = {'Name': 'Zara', 'Age': 7}
# print ("字典长度 : %d" %  len(dict))
# dict.clear()
# print ("字典删除后长度 : %d" %  len(dict))

# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict2 = dict1.copy()
# print("新复制的字典为 : ", dict2)
# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)

# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq)
# print ("新的字典为 : %s" %  str(dict))
# dict = dict.fromkeys(seq, 10)
# print ("新的字典为 : %s" %  str(dict))
# x = {}
# xx = x.fromkeys(['a','b'])
# print(x)
# print(xx)

# dict = {'Name': 'Runoob', 'Age': 27}
# print ("Age 值为 : %s" %  dict.get('Age'))
# print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))

# dict = {'Name': 'Runoob', 'Age': 7}
# # 检测键 Age 是否存在
# if  'Age' in dict:
#     print("键 Age 存在")
# else :
#     print("键 Age 不存在")
# # 检测键 Sex 是否存在
# if  'Sex' in dict:
#     print("键 Sex 存在")
# else :
#     print("键 Sex 不存在")

# dict = {'Name': 'Runoob', 'Age': 7}
# print ("Value : %s" %  dict.items())
# dict = {'Name': 'Runoob', 'Age': 7}
# for i,j in dict.items():
#     print(i, ":\t", j)

# dict = {'Name': 'Runoob', 'Age': 7}
# print ("字典所有的键为 : %s" %  dict.keys())
# phone_book={'sam':'1234','tom':'5678'}  #创建字典
# print(phone_book.keys())                       #调用keys方法
# print(list(phone_book.keys()))                 #调用list函数

# dict = {'Name': 'Runoob', 'Age': 7}
# print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
# print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
# print ("新字典为：", dict)

# dict = {'Name': 'Runoob', 'Age': 7}
# dict2 = {'Sex': 'female' }
# dict.update(dict2)
# print ("更新字典 dict : ", dict)

# dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
# print ("字典所有值为 : ",  list(dict.values()))
# print ("字典所有值为 : ",  dict.values())

# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.pop('name')
# print(pop_obj)
# print(site)

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)