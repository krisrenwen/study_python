
"""
根据如下的学生成绩单完成以下需求:
1:计算每个学生的总分，各科目的平均分，然后一一输出出来
2:统计各科成绩的：最低分，最高分，平均分，并输出
3：查找成绩优秀（平均分大于90分）的学生并且输出出来
"""

def func01():
    # 1:计算每个学生的总分，各科目的平均分，然后一一输出出来
    student = (
        ("s001","王林",85,92,78),
        ("s002","李暮婉",92,88,95),
        ("s003","十三",75,85,82),
        ("s004","曾牛",88,79,91),
        ("s005","周铁",95,96,89),
        ("s006","王卓",76,82,77),
        ("s007","红蝶",81,99,94),
        ("s008","徐立国",75,69,82),
        ("s009","许木",86,89,98),
        ("s010","遁地",66,59,72)
    )

    # 每一个元组里面都是不同的元组,每一行都是都是一个小元组
    print("学号: \t 姓名: \t 中文: \t 英文: \t 数学: \t 总分: \t 平均分: \t")
    for stu in student:
        # 每个学生的总分总分f
        total_score = stu[2] + stu[3] + stu[4]
        #平均分
        average_score = total_score / 3
        # 打印
        print(f"{stu[0]}\t {stu[1]}\t {stu[2]}\t {stu[3]}\t {stu[4]}\t {total_score}\t {average_score:.2f}\t")

# func01()

def func02():
    # 2:统计各科成绩的：最低分，最高分，平均分，并输出
    #  中文: \t 英文: \t 数学
    student = (
        ("s001","王林",85,92,78),
        ("s002","李暮婉",92,88,95),
        ("s003","十三",75,85,82),
        ("s004","曾牛",88,79,91),
        ("s005","周铁",95,96,89),
        ("s006","王卓",76,82,77),
        ("s007","红蝶",81,99,94),
        ("s008","徐立国",75,69,82),
        ("s009","许木",86,89,98),
        ("s010","遁地",66,59,72)
    )
    
    chinese_score = [s[2] for s in student]
    eng_score = [s[3] for s in student]
    math_score = [s[4] for s in student]
    print("----------------------------------")

    #英文成绩的信息
    eng_max = max(eng_score)
    eng_min = min(eng_score)
    eng_avg = sum(eng_score) / len(eng_score)

    #语文成绩信息
    chinese_max = max(chinese_score)
    chinese_min = min(chinese_score)
    chinese_avg = sum(chinese_score) / len(chinese_score)

    #数学成绩
    math_max = max(math_score)
    math_min = min(math_score)
    math_avg = sum(math_score) / len(math_score)

    


