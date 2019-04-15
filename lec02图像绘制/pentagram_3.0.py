"""
    作者：陈思
    功能：五角星的绘制
    版本：3.0
    日期：26/03/2019
    2.0新增功能：加入循环操作
    2.0新增功能：使用递归函数绘制
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

def draw_recursive_pentagram(size):
    """
        迭代绘制五角星
    """
    count = 1
    while count <= 5:
        # 绘制边
        turtle.forward(size)
        turtle.right(144)
        count += 1
    #五角星绘制完成

    size+=10
    if size <=100:
        draw_recursive_pentagram(size)

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
    draw_recursive_pentagram(size)

    turtle.exitonclick()

if __name__ == '__main__':
    main()