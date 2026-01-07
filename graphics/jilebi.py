from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, math

angle = 0          # current angular position (degrees)
spacing = 0.2     # spiral radial spacing per degree
max_angle = 1080   # more loops: 3 full rotations (360 * 3)

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw_circle(x, y, r, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        glVertex2f(x + r * math.cos(math.radians(i)),
                   y + r * math.sin(math.radians(i)))
    glEnd()

def draw():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    step = 0.5
    current = 0.0
    while current <= angle:
        r = current * spacing
        x = r * math.cos(math.radians(current))
        y = r * math.sin(math.radians(current))
        glVertex2f(x, y)
        current += step
    glEnd()

    r = angle * spacing
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))

    draw_circle(x, y, 20, (1, 0, 0))

    glutSwapBuffers()

def animate(value):
    global angle
    angle += 5    # slower speed
    if angle > max_angle:
        angle = 0
    glutPostRedisplay()
    glutTimerFunc(40, animate, 0)  # slower timer: 40 ms

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Spiral Multi-Loop Slower Animation")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()