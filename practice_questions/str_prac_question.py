
"""
第二个案例:
1:输入一个字符串，判断该字符串是否是回文(两边对称)
举例：黄山落叶松叶落山黄
      上海自来水来自海上
"""
def question_01():
    text = input("请输入判断是否是回文的内容: ")
    # 一个从左到右遍历，一个从最后往前遍历
    if text == text[::-1]:
        return True
    else:
        return False
    
# print(question_01())

"""
2：
将用户输入的10个字符串，反转后全部转换成大写，记录在列表中
最后将列表中的内容，遍历输出
"""
# def question_02():
#     #然后准备一个空的列表
#     new_list = []
#     # 先确保用户输入的确实是10个字符串
#     for i in range(10):
#         user_input = input("请输入你的十个字符串: ")
#         #接下来反转这个字符串
#         reverse_text = user_input[::-1]
#         #反转以后接下来就要换成大写
#         upper_text = reverse_text.upper()
#         new_list.append(upper_text)
        
#     for i in new_list:
#         print(i)

def question_02():
    new_list = []
    for i in range(10):
        user_input = input("输入你的十个字符串: ")
        new_list.append(user_input[::-1].upper())
    print(new_list)


# question_02()

"""
邮箱格式验证: 
1：用户输入一个邮箱，验证邮箱格式是否正确(包含一个@,和至少一个".")
2: 如果输入正确的话，输出: "邮箱格式正确"
3: 否则的话，输出: "邮箱格式错误"
"""

def func03():
    # 让用户先输入自己的邮箱
    user_input = input("请输入您的邮箱: ")

    #接下来我们来验证
    #那我们是不是要遍历这个字符串
    
    if (user_input.count("@") == 1) and ("." in user_input):
        print(f"{user_input} 格式正确")
    
    else:
        print(f"{user_input}格式错误，请重新尝试")

func03()
