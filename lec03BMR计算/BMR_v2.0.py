"""
    作者：陈思
    功能：BMR计算器
    版本：2.0
    日期：27/03/2019
"""

def body(a,b,c,d):

    # 判断性别

    if a == '男':
        bmr = (13.7 * b)+(5.0 * c)-(6.8 * d)+66

    elif a == '女':
        bmr = (9.6 * b)+(1.8 * c)-(4.7 * d)+655

    else:
        bmr = -1

    # 结果输出
    if bmr != -1:
        print('基础代谢率为'+str(bmr)+'大卡')
    else:
        print('请输入正确的性别')


def main():
    """
        主函数
    """
    isexit=input('是否退出程序（Y/N）：')

    while isexit == 'N':

        gender = input('请输入性别：')

        weight = float(input('请输入体重（kg）：'))

        height = float(input('请输入身高（cm）：'))

        age = float(input('请输入年龄：'))

        body(gender,weight,height,age)

        print()  #输出空行
        isexit = input('是否退出程序（Y/N）：')


if __name__ == '__main__':
    main()