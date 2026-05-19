
def mock_calculator():
    print("欢迎来到计算机程序!!!")
    num1 = float(input("请输入你的第一个数字: "))
    num2 = float(input("请输入你的第二个数字: "))
    operator = input("请输入你要进行运算的操作符 + - * /: ")
    match operator:
        case "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        case "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        case "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        case "/" if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        case _:
            print("操作不支持")

# mock_calculator()

"""
请编写一个游戏角色移动控制系统，根据用户不同的指令，操控游戏角色执行不同的相应动作(控制台)
玩家输入:         对应的动作:
上 / w / W       向上移动
下 / s / S       向下移动
左 / a / A
右 / d / D
跳 / " "         角色跳跃
攻击/j/J 
退出/esc/ESC     退出游戏
"""
def user_mov_ctrl():
    print("欢迎来到操控动作的游戏!!!")
    while True:
        movement = input("请开始输入你的动作: ")
        match movement:
            case "上" | "w" | "W" :
                print("角色向上移动")
            case "下" | "s" | "S":
                print("角色向下移动")
            case "左" | "a" | "A":
                print("角色向左移动")
            case "右" | "d" | "D":
                print("角色向右移动")
            case "跳" | " ":
                print("角色跳跃")
            case "攻击" | "j" | "J":
                print("角色进行攻击")
            case "退出" | "esc" | "ESC" | "exit" | "EXIT":
                print("退出游戏!!!")
                break
            case _:
                print("未知指令,请重新输入: ")

# user_mov_ctrl()


