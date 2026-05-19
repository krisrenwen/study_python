
# i = 0
# while i < 10:
#     print("思多乱其志，行者皆披靡!!!!")
#     i += 1

# 计算1-100之间所有偶数之和
def sum_of_even():
    sum = 0
    i = 1
    while i <= 100:
        if i % 2 == 0:
            sum += i
        i += 1
    print(sum)

sum_of_even()