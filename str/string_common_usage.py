
"""
常用的这个 string的方法
方法：
1：find() -> 在字符串中查找子字符串，返回第一次出现的索引位置，找不到返回 -1

2: count() -> 统计子字符串中出现的次数

3: upper() ->将字符串中的所有字母！！换成大写

4: lower() -> 将字符串中的所有字母换成小写！！！

5：split() -> 将字符串按照指定分隔符分割成列表

6: strip() -> 去除字符串当中的“空白字符”或者指定的字符

7: replace() -> 将字符串中的指定字符替换成新的子串

8: startwith() -> 检查字符串是否包含指定子串的开头，返回布尔值：true / false
"""

sentence = "Hello -Python-Hello- World"

# 1：find() -> 在字符串中查找子字符串，返回第一次出现的索引位置，找不到返回 -1
index = sentence.find("-")
# print(index)

# 2: count() -> 统计子字符串中出现的次数
c = sentence.count("o")
# print(c)

# 3: upper() ->将字符串中的所有字母！！换成大写
su = sentence.upper()
# print(su)

#4: lower() -> 将字符串中的所有字母换成小写！！！
sl = sentence.lower()
# print(sl)

# 5：split() -> 将字符串按照指定分隔符分割成列表
slist = sentence.split("-")
# print(slist)

# 6: strip() -> 去除字符串当中的“空白字符”或者指定的字符
ss = sentence.strip()
# print(ss)

# 7: replace() -> 将字符串中的指定字符替换成新的子串
sr = sentence.replace("-" , "_")
# print(sr)

#8: startwith() -> 检查字符串是否包含指定子串的开头，返回布尔值：true / false
print(sentence.startswith("Hello"))
print(sentence.endswith("World"))