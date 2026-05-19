
# 列表list切片，截取列表的其中一部分数据作为使用


list1 = [1,2,5,7,8,"hello",True,"define"]
list2 = ["A","C","H","K","L","B","D","x","C","U"]

# 开始索引，结束索引(不包括自身)，步长
print(list1[0:5:1])
print(list1[0:8:2])

print(list2[0:len(list2)])
print(list2[0:5:2])