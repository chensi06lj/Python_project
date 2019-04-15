"""
    作者：陈思
    功能：52周存钱挑战
    版本：1.0
    日期：01/04/2019
"""

def main():

    money_per_week = 10 #起始金额
    i = 1               #周数
    increase_money = 10 #递增金额
    total_week = 52     #总共周数
    saving = 0          #存款

    while i <= total_week:
        saving += money_per_week
        print('当前为第{0}周，存入{1}元，存款为{2}元'.format(i,money_per_week,saving))
        i += 1
        money_per_week += increase_money


if __name__ == '__main__':
    main()