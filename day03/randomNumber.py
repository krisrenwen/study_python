import random


def guess_number_game():
    random_number = random.randint(1,100)
    print("欢迎来到猜数字游戏!!!")
    while True:
        user_guess_number = int(input("请输入一个数字来猜测: "))

        if user_guess_number == random_number:
            print("恭喜猜对了🎉🎉🎉！！！")

        elif user_guess_number < random_number:
            print("数字猜测小了，请重新猜测: ")

        else:
            print("数字猜大了，请重新猜测: ")
            break

def multiple_of_five():
    total = 0
    for i in range(1,1001):
        if i % 5 == 0:
            total += i
    print(total)

#统计字符串，计算有多少a和k
def count_a_and_k():
    sentence = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
    a_count = 0
    k_count = 0
    for i in range(len(sentence)):
        if sentence[i] == "a":
            a_count += 1
        elif sentence[i] == "k":
            k_count += 1
    print(f"a的数量是: {a_count}")
    print(f"k的数量是: {k_count}")

count_a_and_k()
# multiple_of_five()

# guess_number_game()
