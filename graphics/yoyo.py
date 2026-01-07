import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Initial values
r = 40
y = 150
direction = -2  # moving down initially
angle = 0

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-200, 200, -200, 200)

def draw_yoyo():
    # Outer circle (body)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f(r * math.cos(math.radians(i)), r * math.sin(math.radians(i)))
    glEnd()

    # Inner circle (design)
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f((r/2) * math.cos(math.radians(i)), (r/2) * math.sin(math.radians(i)))
    glEnd()

    # Spokes
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for i in range(0, 360, 45):
        theta = math.radians(i)
        glVertex2f(0, 0)
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()

def draw_string():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, 200)
    glVertex2f(0, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_string()

    glPushMatrix()
    glTranslatef(0, y, 0)
    glRotatef(angle, 0, 0, 1)
    draw_yoyo()
    glPopMatrix()

    glFlush()

def animate(value):
    global y, direction, angle

    # Update vertical motion
    y += direction

    # Change direction at limits
    if y <= -200 or y >= 150:
        direction = -direction

    # Spin
    angle += 10
    if angle >= 360:
        angle = 0

    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Yo-Yo Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(30, animate, 0)
    glutMainLoop()

main()
