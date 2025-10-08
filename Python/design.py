import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

# Colors using HSV for smooth rainbow effect
colors = []
num_colors = 36
for i in range(num_colors):
    hue = i / num_colors
    colors.append(colorsys.hsv_to_rgb(hue, 1, 1))

turtle.colormode(1.0)  # Use 0-1 color range

# Draw flower-like pattern
for i in range(360):
    t.color(colors[i % num_colors])
    t.circle(120)
    t.left(10)   # rotate for each petal
    t.forward(10)

turtle.done()