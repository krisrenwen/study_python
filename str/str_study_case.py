
"""
第二个案例:
1:输入一个字符串，判断该字符串是否是回文(两边对称)
举例：黄山落叶松叶落山黄
      上海自来水来自海上

2：
将用户输入的10个字符串，反转后全部转换成大写，记录在列表中
最后将列表中的内容，遍历输出
"""
def recursive_statement():
    sentence = input("请输入你的文字内容: ")
    if sentence == sentence[::-1]:
        print(sentence)
        

# recursive_statement()


def reverse_cap_letters():
    text = input("请输入10个字符串: ")
    text_len = len(text)
    my_list = []
    if text_len == 10:
        reverse_text = text[::-1]
        upper_text = reverse_text.upper()
        my_list.append(upper_text)
        for i in my_list:
            print(i)
        
    else:
        print(f"您输入的字符串长度为: {text_len} 不合法")

# reverse_cap_letters()



"""
邮箱格式验证: 
1：用户输入一个邮箱，验证邮箱格式是否正确(包含一个@,和至少一个".")
2: 如果输入正确的话，输出: "邮箱格式正确"
3: 否则的话，输出: "邮箱格式错误"
"""

#方式2：
def email_format_authentication02():
    user_email = input("请输入您的邮箱地址: ")
    if (user_email.count("@") == 1) and ("." in user_email):
        print(f"{user_email}是合法的，邮箱格式正确")
    else:
        print(f"{user_email}是不合法的，邮箱格式错误")

#方式1：
def email_format_authentication():
    user_email = input("请输入您的邮箱地址: ")
    #然后我们需要来判断是否格式正确
    if (user_email.count("@") == 1) and (user_email.count(".") >= 1):
        print(f"{user_email}是合法的，邮箱格式正确")
    else:
        print(f"{user_email}是不合法的，邮箱格式错误")


# email_format_authentication()