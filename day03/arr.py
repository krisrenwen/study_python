
"""
list列表的好处在于可以一次行存储多个数据（元素）
注意，可以存储不同类型的数据
可以重复，元素可以修改，有序的
"""
score_list = [1,23,4,5,6,7,"true","false"]
print(score_list)

#修改元素
score_list[0] = "被我修改了的元素"
print(score_list)

#删除元素
del score_list[2]
print(score_list)

#如何遍历列表
for item in score_list:
    print(item, end=" ")
