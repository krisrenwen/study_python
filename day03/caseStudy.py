
"""
需求：根据输入的用户名密码执行登录操作，具体要求如下：
正确的用户名和密码是：admin/666888, zhangsan/123456, taoge/888666
输入用户名和密码直到登陆成功，程序执行结束，如果登陆失败，则继续输入用户名和密码进行登录
输入的用户名和密码不能为空！
登录成功输出："登录成功，进入b站首页~"
登录失败输出："用户名或密码错误，请重新输入!"
"""

def login_password_authentication():
    while True:
        user_name = input("请输入您的账号名: ")
        user_password = str(input("请输入您的账号密码: "))
        
        if user_name == "" or user_password == "":
            break;
        if user_name == "admin" and user_password == "666888":
            print("登录成功，进入b站首页~")
            break
        elif user_name == "zhangsan" and user_password == "123456":
            print("登录成功，进入b站首页~")
            break
        elif user_name == "taoge" and user_password == "888666":
            print("登录成功，进入b站首页~")
            break
        else:
            print("用户名或密码错误，请重新输入!")
            

login_password_authentication()

