
# string = input("请输入要遍历的字符串: ")
#
# for s in string:
#     print(s,end="")

"""
for 元素 in 待处理的数据集:
    循环体语句（对元素的处理）
"""

"""
range语句
用法一 ： range(end) -> 从0开始，到end结束的数字序列（不包含end本身！）
range(5) -> 0,1,2,3,4

用法2: range(start,end) -> 从start开始，到end结束的数字序列，不包含end本身！
range(2,8) -> 2,3,4,5,6,7

用法3: range(start,end,step) -> 从start开始，到end结束的数字序列，不包括end本身，step是步长
range(0,10,2) -> 就是0,2,4,6,8
"""

#打印1到100的奇数之和
def sum_of_odd():
    total = 0
    for i in range(1,101):
        if i % 2 == 1:
            total += i

    print(f"sum is: {total}")


# 计算100到500之间的所有3的倍数的数字之和
def sum_multiple_of_three():
    total = 0
    for i in  range(100,501):
        if i % 3 == 0:
            total += i
    print(f"sum is: {total}")


def printing_of_square():
    m = int(input("请输入方形的行: "))
    n = int(input("请输入方形的列: "))
    for i in range(m):
        for j in range(n):
            print("*",end=" ")
        print()

# 打印9x9的乘法表
def multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j} * {i} = {i * j}", end="\t")
        print()



# printing_of_square()
# sum_multiple_of_three()
# sum_of_odd()
# multiplication_table()


