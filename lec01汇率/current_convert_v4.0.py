"""
    作者：陈思
    功能：汇率兑换
    版本：3.0
    日期：21/03/2019
    2.0新增功能：根据输入判断货币类型
    3.0新增功能：程序一致运行，用户选择退出
    4.0新增功能：函数封装
"""

def convery_currency(im, er):

    """
        汇率兑换函数
    """
    out = im * er
    return out

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：')

# 获取货币单位
unit = currency_str_value[-3:]

#判断货币单位，运算兑换金额
if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])

    # 调用函数
    out_money = convery_currency(in_money, exchange_rate)
    print('兑换后金额：', out_money)

else:
    print('不支持该货币兑换')




