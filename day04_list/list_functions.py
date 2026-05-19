
"""
list的诸多函数：
1: append() -> 在列表尾部追加元素
2: insert() -> 在指定的索引前面插入元素
3: remove() -> 移除中第一个匹配的值
4: pop() -> 删除列表中指定索引为止的元素，如果没指定索引的话，默认是删除末尾第一个
5: sort() -> 对列表进行排序，列表中的元素类型必须一致
6: reverse() ->对元素列表进行反转
"""

list1 = [10,20,90,70,1,55,434]
print(list1)

list1.append(999)
print(list1)

list1.insert(0,777)
print(list1)

list1.remove(1)
print(list1)

pop_ele = list1.pop()
print(pop_ele)

list1.sort()
print(list1)

list1.reverse()
print(list1)