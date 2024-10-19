# week 3/DayDayUpQ4.py
"""
This script defines a function `dayUP` that calculates the growth factor over a year, taking into account a daily increase factor and a decrease on weekends. It then iterates to find the minimum daily effort factor required for the growth to exceed 37.78 times the initial value within a year.
"""
# 这段代码定义了一个函数dayUP，它接受一个参数growth_factor，代表每天努力工作的增长因子。函数的目的是计算一年后的成长值，考虑到每周有一天不努力（周末），在这一天成长值会下降1%。代码的逻辑是这样的：
def dayUP(growth_factor):
# 初始化成长值dayup为1。
    dayup = 1
# 使用一个for循环遍历365天。
    for i in range(365):
# 在循环中，使用if语句检查当前天数是否是周末（即i % 7的结果是6或者0，因为Python中星期天是0开始）。
        if i % 7 in [6, 0]:
# 如果是周末，则成长值乘以1 - 0.01，即下降1%。
            dayup = dayup * (1 - 0.01)
        else:
# 如果不是周末，则成长值乘以1 + growth_factor，即增长growth_factor的百分比。
            dayup = dayup * (1 + growth_factor)
    return dayup
# 代码设置了一个变量dayfactor并初始化为0.01
dayfactor = 0.01
# 接下来的while循环是用来寻找一个合适的dayfactor值，使得一年后的成长值至少为37.78。循环的条件是dayUP(dayfactor) < 37.78，即当计算出的成长值小于37.78时，循环继续。
while dayUP(dayfactor) < 37.78:
# 在循环体内，dayfactor每次增加0.001，然后再次调用dayUP函数计算成长值。
    dayfactor += 0.001
# 最后，当找到满足条件的dayfactor时，使用print函数输出结果，保留三位小数。
print("工作日的努力参数是：{:.3f}".format(dayfactor))
    