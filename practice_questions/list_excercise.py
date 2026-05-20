
# 生成 1-20的平方列表
def multiple_of_20():
    num_list = [i ** 2 for i in range(1,21)]
    print(num_list)

# multiple_of_20()

"""
从如下的数字列表中提取所有偶数，并计算其平方，组成一个新的列表打印出来
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
"""
def square_of_all_even():
    num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
    new_list = [i ** 2 for i in num_list if i % 2 == 0]
    print(new_list)

# square_of_all_even()

"""
合并两个列表中的元素，然后进行去重操作
    list1 = [19,23,54,64,875,20,109,232,123,54]
    list2 = [55,80,72,35,60,123,54,29,91]
"""
def merge_two_list():
    list1 = [19,23,54,64,875,20,109,232,123,54]
    list2 = [55,80,72,35,60,123,54,29,91]
    list_1 = list1 + list2
    new_list = []
    for i in list_1:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    print(new_list)

# merge_two_list()

"""
将用户输入的十个数字存放到列表中
然后将列表的数字进行排序，
输出其中最小值，最大值，和平均值
"""
def avg_min_max():
    numlist = []
    for i in range(10):
        txt = int(input("请输入十个数字: "))
        numlist.append(txt)
    numlist.sort()
    print(f"最小值为: {numlist[0]}")
    print(f"最大值为: {numlist[-1]}")
    print(f"平均值为: {sum(numlist)/len(numlist)}")
    
    
# avg_min_max()

"""
将如下多个列表合并为一个列表，并进行去重操作
list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
list2 = ['X','Z','T','Y','D','E','F','G']
排序好（升序）后输出到控制台
"""

def question_01():
    list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
    list2 = ['X','Z','T','Y','D','E','F','G']
    tmp_list = list1 + list2
    new_list = []
    for num in tmp_list:
        if num not in new_list:
            new_list.append(num)
    new_list.sort()
    print(new_list)

# question_01()

"""
将如下列表中可以被 “3” 或者 “5” 整除的元素提取出来
并且获取这些数字对应的平方，组成一个新的列表
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        25,26,27,28,29,30]
"""
def question_02():

    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        25,26,27,28,29,30]
    
    new_list = [num ** 2 for num in list1 if (num % 3 == 0) and (num % 5 == 0)]
    print(new_list)

# question_02()

"""
将如下的列表正数提取出来，封装成一个新的列表
list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,39]
"""
def question_03():
    list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,39]
    new_list = [num for num in list1 if num >= 0]
    print(new_list)

# question_03()



    