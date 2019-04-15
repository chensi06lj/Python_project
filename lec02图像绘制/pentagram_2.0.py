"""
    作者：陈思
    功能：五角星的绘制
    版本：2.0
    日期：25/03/2019
    2.0新增功能：加入循环操作
"""

import turtle

def draw_pentagram(size):
    """
    绘制五角星
    """
    count = 1
    while count <= 5:
        # 绘制边
        turtle.forward(size)
        turtle.right(144)
        count += 1             # 简写：+= -= *= /=

def main():
    """
        主函数
    """
   #声明边长

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('gold')

    size = 50
    while size <= 100:
        #调用函数
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()

if __name__ == '__main__':
    main()