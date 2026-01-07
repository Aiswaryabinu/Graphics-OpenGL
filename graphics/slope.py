import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

r = 40
x = -250
y = 190
xc = 2
angle = 0
wheel_angle = 0
m = ((-250) - 190) / (200 - (-250))

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-300, 300, -300, 300)

def circle():
    glColor3f(0, 0, 0.9)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f(r * math.cos(math.pi * i / 180),
                   r * math.sin(math.pi * i / 180))
    glEnd()

    # spokes
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, 40)
    glVertex2f(0, -40)
    glVertex2f(-40, 0)
    glVertex2f(40, 0)
    glEnd()

def slope():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-250, 190)
    glVertex2f(200, -250)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    slope()

    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(-wheel_angle, 0, 0, 1)  # rotation opposite to movement
    circle()
    glPopMatrix()

    glFlush()

def animate(value):
    global x, y, m, xc, wheel_angle

    # Move along slope
    x += xc
    if x >= 200:
        x = -250

    # Calculate y using slope equation
    y = m * (x - (-250)) + 190

    # Calculate rotation based on distance traveled
    distance = math.sqrt(xc**2 + (m * xc)**2)
    rotation_per_frame = (distance / (2 * math.pi * r)) * 360
    wheel_angle += rotation_per_frame
    if wheel_angle >= 360:
        wheel_angle -= 360

    glutPostRedisplay()
    glutTimerFunc(40, animate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Rolling Wheel Down Slope")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(40, animate, 0)
    glutMainLoop()

main()
