
# 字符串也是可以进行切片的
"""
语法就是 [下标起始,结束下表(不包括结束下标本身,步长)]
"""

sentence = "Hello - python"
print(sentence[0:7:1])
print(sentence[4])

greeting = "hello world !!! I am Kris !!!"

"""字符串也可以循环遍历"""
for i in sentence:
    print(i, end=" ")

print("hello github")