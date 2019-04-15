"""
    作者：陈思
    日期：09/04/2019
    功能：输入某年某月某日，判断第几天
"""

from datetime import datetime

def main():
    """
        主函数
    """

    input_date_str = input('请输入年月日（yyyy/mm/dd）:')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day
    day_in_year_tup = (31,28,31,30,31,30,31,31,30,31,30,31)

    #计算之前每月天数总和，再加上当月天数
    days = sum(day_in_year_tup[:month-1]) + day

    if (year%4 == 0 and year%100 != 0 ) or year%400 == 0 :
        if month > 2:
            days += 1
            print('第{}天'.format(days))
        else:
            print('第{}天'.format(days))
    else:
        print('第{}天'.format(days))

if __name__ == '__main__' :
    main()