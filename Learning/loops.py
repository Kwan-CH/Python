# import turtle

## draw polygon with inner polygon with user input
# def draw_polygon(side):
#     turtle.penup()
#     turtle.goto(-80, -100)
#     turtle.pendown()
#     turtle.tracer(0, 0)
#     for steps in range(side):
#         turtle.forward(100)
#         turtle.left(360 / side)
#         for inner_polygon in range(side):
#             turtle.forward(50)
#             turtle.left(360 / side)
#     turtle.update()
#
#
# polygon = int(input('how many side of your polygon is: '))
# draw_polygon(polygon)
# turtle.exitonclick()


## draw polygon with user input until user stop
# [60, 90, 108, 120, 128.57, 135, 140, 144]
# def while_draw_polygon():
#     pen_color = input('what color you want for the pen: ').lower()
#     line_length = int(input('what side length you want: '))
#     while line_length != 0:
#         inner_angle = float(input('what is the inner angle for the polygon: '))
#         side = 360 / (180 - inner_angle)
#         turtle.clear()
#         turtle.color(pen_color)
#         for steps in range(int(side)):
#             turtle.forward(line_length)
#             turtle.left(180 - inner_angle)
#         line_length = int(input('what side length you want: '))
#
#
# while_draw_polygon()
# turtle.exitonclick()

"""pass statement is to maintain syntactic structure
do not have any action
continue will skip the remaining code in a loop"""

for i in range(0, 9):
    if i == 2:
        continue
    print(i)

