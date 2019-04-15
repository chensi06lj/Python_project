"""
    作者：陈思
    功能：汇率兑换
    版本：1.0
    日期：19/03/2019
"""

# 汇率
USD_VS_RMB = 6.77

# 输入人民币
rmb_str_value = input('请输入人民币（CNY）金额：')

# 将字符串转换为数字
rmb_value = eval(rmb_str_value)

# 求兑换美元
usd_value = rmb_value / USD_VS_RMB

print('美元（USD）金额是：', usd_value)
