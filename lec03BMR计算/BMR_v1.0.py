"""
    作者：陈思
    功能：BMR计算器
    版本：1.0
    日期：27/03/2019
"""

def main():
    """
        主函数
    """
    pass

    # 性别
    gender = '男'

    # 体重
    weight = 70

    # 身高
    height = 175

    # 年龄
    age = 30

    if gender == '男':
        bmr = (13.7 * weight)+(5.0 * height)-(6.8 * age)+66

    elif gender == '女':
        bmr = (9.6 * weight)+(1.8 * height)-(4.7 * age)+655

    else:
        bmr = -1


    if bmr != -1:
        print('基础代谢率为',bmr)
    else:
        print('请输入正确的性别')

if __name__ == '__main__':
    main()