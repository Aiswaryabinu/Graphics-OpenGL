from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

angle = 0
direction = 1
boat_x = -250
oar_angle = 0
oar_direction = 1

def init():
    glClearColor(0.5, 0.8, 1.0, 1)  # sky blue
    gluOrtho2D(-300, 300, -200, 200)

def draw_boat():
    glColor3f(0.4, 0.2, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-40, -20)
    glVertex2f(40, -20)
    glVertex2f(30, -35)
    glVertex2f(-30, -35)
    glEnd()

def draw_person():
    # body
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, -10)
    glVertex2f(0, 20)
    glEnd()

    # head
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(0 + 5 * math.cos(math.radians(i)), 25 + 5 * math.sin(math.radians(i)))
    glEnd()

def draw_oar():
    glPushMatrix()
    glTranslatef(10, -15, 0)  # pivot point
    glRotatef(oar_angle, 0, 0, 1)
    glColor3f(0.5, 0.3, 0.1)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(60, -10)
    glEnd()
    glPopMatrix()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(boat_x, 0, 0)

    draw_boat()
    draw_person()
    draw_oar()

    glPopMatrix()
    glFlush()

def update(value):
    global boat_x, oar_angle, oar_direction

    # Move boat forward slowly
    boat_x += 0.5
    if boat_x > 300:
        boat_x = -300

    # Animate oar (row only one side)
    oar_angle += 3 * oar_direction
    if oar_angle > 30 or oar_angle < -10:
        oar_direction *= -1

    glutPostRedisplay()
    glutTimerFunc(40, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"One-Side Rowing Animation")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(40, update, 0)
    glutMainLoop()

main()
