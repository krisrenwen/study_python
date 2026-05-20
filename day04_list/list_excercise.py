
"""
生成 1-20的平方列表
"""
# def generate_multi():
#     # 我先生成一个空列表，然后每一次将1到20的每一个平方都放到列表中
#     num_list = []
#     for i in range(1,21):
#         #要习惯这个写法
#         num_list.append(i ** 2)

#     print(num_list)
def generate_square():
    #如果我要生成列表的平方的话我需要计算每一个1~20的平方
    #然后放到一个空的列表中
    #尝试一下列表推导式
    num_list = [num ** 2 for num in range(1,21)]
    print(num_list)

# generate_multi()

"""
方法2: 用python的列表推导式来进行计算
    列表推导式的语法格式: [要插入的值 for i in (序列，或者列表)]
"""
def generate_multi_version2():
    num_list2 = [i ** 2 for i in range(1,21)]
    print(num_list2)

# generate_multi_version2()

"""
从如下的数字列表中提取所有偶数，并计算其平方，组成一个新的列表打印出来
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
"""

# def cal_even_multiple_of_list():
#     num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
#     new_list =[]
#     # 那我首先要先遍历这个列表，然后找出所有的偶数
#     # 然后放到新的列表中
#     for num in num_list:
#         if num % 2 == 0:
#             new_list.append(num * num)
#     print(new_list) 

def find_square_of_even():
    num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
    #我要去找所有的偶数，这是第一个要求
    #第二个要求就是找出这些偶数以后计算平方
    #最后打印出新的列表
    new_list = [num ** 2 for num in num_list if num % 2 == 0]
    print(new_list)

# cal_even_multiple_of_list()

"""
试一下这个列表推导式的写法
语法: [要插入的值 for i in (序列，或者列表) 后面可以跟 "条件判断"]
"""
def cal_even_mul_list2():
    num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
    new_list = [num ** 2 for num in num_list if num % 2 == 0]
    print(new_list)

cal_even_mul_list2()

"""
合并两个列表中的元素，然后进行去重操作
"""

def merge_list_unique():
    list1 = [19,23,54,64,875,20,109,232,123,54]
    list2 = [55,80,72,35,60,123,54,29,91]
    #我首先要先合并两个列表到一个列表中
    num_list = list1 + list2
    print("现在合并后的元素列表：", num_list)
    new_list = []
    for num in num_list:
        if num not in new_list:
            new_list.append(num)
    print(new_list)

def remove_repeat_elements():
    list1 = [19,23,54,64,875,20,109,232,123,54]
    list2 = [55,80,72,35,60,123,54,29,91]
    # 合并列表
    # 解包 -> 将容器解开成一个个独立的元素
    # num_list1 = [*list1,*list2]

    #直接将两个列表拼接也可以
    num_list1 = list1 + list2

    #这两步还可以简化
    # for num in list2:
    #     list1.append(num)
    #将list2的元素放入到list1当中的元素
    print("list1现在的元素: ",num_list1)
    #然后现在可以进行去除重复排序
    new_list = []
    for num in num_list1:
        #判断new_list[]是否存在num元素，如果不存在再添加
        if num not in new_list:
            new_list.append(num)
    print(new_list)


# remove_repeat_elements()

"""
将用户输入的十个数字存放到列表中
然后将列表的数字进行排序，
输出其中最小值，最大值，和平均值
"""

def my_func():
    #先定义一个空列表
    num_list = []

    #然后让用户输入十个数字，并给出提示
    for i in range(10):
        # 用一个变量每次接收一个变量，后续放入到列表中
        # 这里的input()函数接受的是str类型，需要转换到int类型
        num = int(input("请输入十个数字: "))
        #每添加一个数字以后我需要放到列表中[]
        num_list.append(num)
    # 循环结束，10个数字都放到空列表里了

    # 现在把列表进行排序
    num_list.sort()
    print("排序好的列表是: ",num_list)
    
    #然后现在找出最小值
    print("最小值是: ",num_list[0])

    #然后输出最大值
    print("最大值是: ",num_list[-1])

    #然后输出平均值
    print("平均值是: ",sum(num_list)/len(num_list))



# my_func()



