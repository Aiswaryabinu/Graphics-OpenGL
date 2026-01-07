from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random

'''
1. rightlekk povumbo kann in right, angle in anticlockwise, so 20,340 (not fully closed mouth)
2.pinne tirich clockwise
3.random() useythatt food particles avdem ivdem vechu
4.pinne angadum ingadum oodichu.
5.foodlu ethumbo oru eating pole vaya kooti, angle kooti
6.then food disappear aaki
7.then next food spot set akki, food reapear akki.
8. that's it
'''


pac_x = -200
pac_y = 0
pac_speed = 1
mouth_angle = 360
food_x = 0
food_y = 0
food_visible = True
dir = 1
facing_right = True
mouth_closing = False
mouth_opening = False

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)

def draw_pacman(x, y, angle):
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)

    if facing_right:
        start, end = 20, 340 
    else:
        start, end = 200, 520  

    for i in range(int(start + (360 - angle) / 2), int(end - (360 - angle) / 2)):
        theta = math.radians(i)
        glVertex2f(x + 30 * math.cos(theta), y + 30 * math.sin(theta))
    glEnd()

def draw_eye():
    global pac_x, pac_y, facing_right
    glColor3f(0, 0, 0)
    glPointSize(5)
    glBegin(GL_POINTS)
    if facing_right:
        glVertex2f(pac_x + 10, pac_y + 20)
    else:
        glVertex2f(pac_x - 10, pac_y + 20)
    glEnd()

def draw_line():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-250, 0)
    glVertex2f(250, 0)
    glEnd()

def draw_food(x, y):
    if food_visible:
        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(x - 5, y - 5)
        glVertex2f(x - 5, y + 5)
        glVertex2f(x + 5, y + 5)
        glVertex2f(x + 5, y - 5)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    draw_food(food_x, food_y)
    draw_pacman(pac_x, pac_y, mouth_angle)
    draw_eye()
    glutSwapBuffers()

def update(value):
    global pac_x, mouth_angle, food_visible, food_x, dir, facing_right, mouth_closing, mouth_opening

    pac_x += pac_speed * dir

    if pac_x >= 250:
        dir = -1
        facing_right = False
    elif pac_x <= -250:
        dir = 1
        facing_right = True

    if food_visible and abs(pac_x - food_x) < 10:
        mouth_opening = True
        food_visible = False

    if mouth_opening:
        mouth_angle -= 3
        if mouth_angle <= 300:
            mouth_angle = 300
            mouth_opening = False
            mouth_closing = True  

    if mouth_closing:
        mouth_angle += 3
        if mouth_angle >= 350:
            mouth_angle = 350
            mouth_closing = False
            food_x = random.uniform(-200, 200)
            food_visible = True

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    global food_x, food_y
    food_x = random.uniform(-200, 200)
    food_y = 0
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Pocker Mon")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()