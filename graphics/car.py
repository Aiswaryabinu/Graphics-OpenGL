from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

car_x = -200   # starting X position of car
wheel_angle = 0   # wheel rotation

def drawcircle(x, y, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361):
        glVertex2f(x + r * math.cos(math.pi * i / 180),
                   y + r * math.sin(math.pi * i / 180))
    glEnd()

def draw_wheel(x, y, r):
    glColor3f(1, 0, 0)
    drawcircle(x, y, r)
    glColor3f(0, 0, 1)
    drawcircle(x, y, r / 3)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for i in range(4):
        theta = math.radians(wheel_angle + i * 90)
        glVertex2f(x, y)
        glVertex2f(x + r * math.cos(theta), y + r * math.sin(theta))
    glEnd()

def body():
    global car_x
    glClear(GL_COLOR_BUFFER_BIT)

    # car body (bottom rectangle)
    glColor3f(0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(car_x, 100)
    glVertex2f(car_x + 200, 100)
    glVertex2f(car_x + 200, 150)
    glVertex2f(car_x, 150)
    glEnd()

    # car top (yellow)
    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(car_x + 50, 150)
    glVertex2f(car_x + 150, 150)
    glVertex2f(car_x + 130, 200)
    glVertex2f(car_x + 70, 200)
    glEnd()

    # wheels
    draw_wheel(car_x + 50, 90, 20)
    draw_wheel(car_x + 150, 90, 20)

    glutSwapBuffers()  # ✅ for double buffering

def update(value):
    global wheel_angle, car_x
    car_x += 5
    wheel_angle -= 15
    if wheel_angle <= -360:
        wheel_angle = 0
    if car_x > 600:
        car_x = -200
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

def init():
    glClearColor(0.3, 0.3, 0.3, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 400)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"Car Animation with Horn")
    init()
    glutDisplayFunc(body)
    glutTimerFunc(30, update, 0)
    glutMainLoop()

main()
