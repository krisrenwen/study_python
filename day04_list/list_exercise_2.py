
"""
将如下多个列表合并为一个列表，并进行去重操作
list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
list2 = ['X','Z','T','Y','D','E','F','G']
排序好（升序）后输出到控制台
"""
def func_01():
    list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
    list2 = ['X','Z','T','Y','D','E','F','G']
    # 那首先我先要将两个列表的元素拼接成为一个
    #在python里面可以使用 "+"进行拼接列表
    #拼接完成以后进行去重复的操作
    new_list = []
    list1 = list1 + list2
    for num in list1:
        if num not in new_list:
            new_list.append(num)
    #拼接完成以后需要排序，升序
    new_list.sort()
    print(new_list)

# func_01()


"""
将如下列表中可以被 “3” 或者 “5” 整除的元素提取出来
并且获取这些数字对应的平方，组成一个新的列表
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        25,26,27,28,29,30]
"""
def func_02():
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
             25,26,27,28,29,30]
    
    new_list = [num ** 2 for num in list1 if (num % 3 == 0) and (num % 5 == 0)]
    print(new_list)

# func_02()

"""
将如下的列表正数提取出来，封装成一个新的列表
list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,39]
"""
def func_03():
    list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,39]
    # new_list = []
    # for num in list1:
    #     if num >= 0:
    #         new_list.append(num)
    # print(new_list)

    #可以尝试下列表推导式
    new_list = [num for num in list1 if num >= 0]
    print(new_list)

# func_03()

