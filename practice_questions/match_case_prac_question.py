
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

def game_control_movement():
    print("欢迎来到操控角色动作的游戏")
    while True:
        movement = input("请输入你要进行的操作: ")
        match movement:
            case "上" | "w" | "W":
                print("角色向上移动")

            case "下" | "s" | "S":
                print("角色向下移动")

            case "左" | "a" | "A":
                print("角色向左移动")
            
            case "d" | "右" | "D":
                print("角色向右移动")
            
            case " " | "条":
                print("角色进行跳跃")

            case "j" | "J":
                print("角色进行攻击")

            case "退出" | "esc" | "Esc":
                print("退出游戏")
                break

            case _:
                print("为止指令，请重新输入: ")

game_control_movement()