"""
    作者：陈思
    日期：15/04/2019
    功能：输入某年某月某日，判断第几天
    2.0新增功能：用列表替换元组
"""

from datetime import datetime

def is_leap_year(year):
    """
        判断是否闰年，返回真假值
    """
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True

    return is_leap


def main():
    """
        主函数
    """

    input_date_str = input('请输入年月日（yyyy/mm/dd）:')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day
    day_in_year_list = [31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap_year(year):
        day_in_year_list[1] = 29  #列表可直接替换2月份的天数（元组不可重新赋值）

    #计算之前每月天数总和，再加上当月天数
    days = sum(day_in_year_list[:month-1]) + day


    # if is_leap_year(year) and month > 2:
    #     days += 1

    print('第{}天'.format(days))

if __name__ == '__main__' :
    main()