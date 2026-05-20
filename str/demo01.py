
# 字符串也是可以进行切片的
"""
语法就是 [下标起始,结束下表(不包括结束下标本身,步长)]
"""

sentence = "Hello - python"
# 这里的语法就是[下标起始的位置，然后结束下标(不包括自身)，然后步长多少]
print(sentence[0:7:1])
print(sentence[4])


"""字符串也可以循环遍历"""
for i in sentence:
    print(i, end=" ")

print("hello github")