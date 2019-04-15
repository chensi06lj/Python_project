"""
    作者：陈思
    功能：汇率兑换
    版本：3.0
    日期：21/03/2019
    2.0新增功能：根据输入判断货币类型
    3.0新增功能：程序一致运行，用户选择退出
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：')

i=0

while currency_str_value != 'Q':

    i = i + 1
    print('循环次数', i)

    #获取货币单位
    unit = currency_str_value[-3:]

    #判断货币单位，运算兑换金额
    if unit == 'CNY':
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_VS_RMB
        print('美元（USD）金额是：', usd_value)

    elif unit == 'USD':
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB
        print('人民币（CNY）金额是：', rmb_value)

    else:
        print('输入货币单位错误')

    print('**********************************************')

    # 带单位的货币输入
    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）：')



print('程序已退出')