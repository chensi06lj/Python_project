"""
    作者：陈思
    功能：递归函数-分形树的绘制
    版本：1.0
    日期：26/03/2019

"""

import turtle

def draw_branch(branch_length):
    """
        绘制分形树
    """
    if branch_length > 5:

        #绘制右侧树枝
        turtle.forward(branch_length)
        print('向前',branch_length)
        turtle.right(20)
        print('右转',20)
        draw_branch(branch_length-15)
        if branch_length-30 < 0 :
            turtle.color('green')

        #绘制左侧树枝
        turtle.left(40)
        print('左转', 40)
        draw_branch(branch_length-15)
        if branch_length-30 < 0 :
            turtle.color('green')

        #返回之前树枝
        turtle.right(20)
        print('右转', 20)
        turtle.backward(branch_length)
        print('向后', branch_length)
        turtle.color('red')

def main():
    """
        主函数
    """
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.color('red')
    turtle.left(180)
    draw_branch(100)
    turtle.exitonclick()

if __name__ == '__main__':
    main()