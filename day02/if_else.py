
def score_grade():
    score = int(input("请输入你的成绩: "))
    if score >= 85:
        print(f"您的成绩为：{score},属于优等")
    elif 60 <= score <= 85:
        print(f"您的成绩为: {score},属于及格范围")
    else:
        print(f"您的成绩为:{score},很遗憾不及格")

# score_grade()

def purchase_discount():
    amount = float(input("请输入您的总金额来计算你的折扣: "))
    if amount >= 500:
        print("您可以享受到8折优惠")
    elif 300 <= amount < 500:
        print("您可以享受到9折优惠")
    elif 100 <= amount < 300:
        print("您可以享受到95折")
    else:
        print("不好意思，您享受不到任何的优惠")

# purchase_discount()

# 用电计算单位
def count_electricity_bill() :
    electricity = float(input("请输入您的电量来计算费用: "))
    if electricity < 2880:
        bill = electricity * 0.4883
        print(f"您的电量为: {electricity},费用为: {bill:.2f}")
    elif 2880 <= electricity <= 4800:
        bill = electricity * 0.5383
        print(f"您的电量为: {electricity},费用为: {bill:.2f}")
    else:
        bill = electricity * 0.7883
        print(f"您的电量为: {electricity},费用为: {bill:.2f}")

# count_electricity_bill()

# def mock_calculator():
#     num1 = float(input("请输入第1个数字: "))
#     num2 = float(input("请输入第2个数字: "))
#     operator = input("请输入你要运算的 + - * / % 运算符: ")
#     match operator:
#         case "+":
#             print(f"{num1} + {num2}的结果是: {num1 + num2}")
#         case "-":
#             print(f"{num1} - {num2} = {num1 - num2}")
#         case "*":
#             print(f"{num1} * {num2} = {num1 * num2}")
#         case "%":
#             print(f"{num1} % {num2} = {num1 % num2}")
#         case "/" if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         case _:
#             print("操作不支持")
#
# mock_calculator()
