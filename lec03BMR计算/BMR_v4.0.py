"""
    作者：陈思
    功能：BMR计算器
    版本：4.0
    日期：28/03/2019
    3.0新增功能：多个输入
    4.0新增功能：异常处理
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
        print('您的性别：{0}，体重：{1}公斤，身高：{2}厘米，年龄：{3}岁'.format(a,b,c,d))  #{数字}，可指定format的位置
        print('基础代谢率为：{}大卡'.format(bmr))  # 效果等同于：print('基础代谢率为'+str(bmr)+'大卡')

    else:
        print('请输入正确的性别')


def main():
    """
        主函数
    """
    isexit=input('是否退出程序（Y/N）：')

    while isexit == 'N':

        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重 身高 年龄： ')
        str_list = input_str.split(' ')  #字符串分割，生成列表

        # 异常处理
        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = float(str_list[3])

            #调用函数
            body(gender, weight, height, age)

        except ValueError:
            print('请输入正确的信息！')
        except IndexError:
            print('输入信息过少！')
        except:  #其他错误
            print('程序异常！')

        print()  # 输出空行
        isexit = input('是否退出程序（Y/N）：')


if __name__ == '__main__':
    main()