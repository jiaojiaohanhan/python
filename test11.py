# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])
# print ("dict['Class']: ", dict['Class'])

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'};
# print("dict['Alice']: ", dict['Alice'])

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8;               # 更新 Age
# dict['School'] = "菜鸟教程"  # 添加信息
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del dict['Name'] # 删除键 'Name'
# dict.clear()     # 清空字典
# del dict         # 删除字典
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print ("dict['Name']: ", dict['Name'])

# dict = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(len(dict))
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(str(dict))
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(type(dict))

cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for i in cities['北京']:
    print(i)
for i in cities['北京']['海淀']:
    print(i)