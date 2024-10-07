# PythonDraw.py
import turtle # import保留字，引入了一个绘图库。名字叫做：turtle(海龟)
turtle.setup(650,350,200,200) # -setup()设置窗体大小及位置，4个参数中后两个可选 (turtle.setup(width, height, startx, starty)); x is the width between the left side of the drawing frame and the left side of the monitor; y is the distance between the top side of the drawing frame and the top side of the monitor 
turtle.penup() # 别名turtle.pu() 抬起画笔，海龟在飞行
turtle.fd(-250) # formal name turtle.forward()
turtle.pendown() # 别名turtle.pd() 落下画笔，海龟在爬行
turtle.pensize(25) # 别名turtle.width(width) 画笔宽度，海龟的腰围
turtle.pencolor('purple') # 画笔颜色，海龟在涂装 通过颜色字符串或r,g,b值实现
turtle.seth(-40) # formal name turtle.setheading(angle)
for i in range(4): # range(数字)，数字表示循环的次数
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done() # 程序运行后不会自动退出，需要手动退出