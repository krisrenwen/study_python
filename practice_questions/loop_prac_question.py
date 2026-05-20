
# 打印1到100的奇数之和
def sumOfOdd():
    sum = 0
    for i in range(1,101):
        if i % 2 == 1:
            sum += i
    print(sum)

# sumOfOdd()

# 计算100到500之间的所有3的倍数的数字之和
def sum_multi_of_three():
    sum = 0
    for i in range(100,501):
        if i % 3 == 0:
            sum += i
    print(sum)

sum_multi_of_three()

            