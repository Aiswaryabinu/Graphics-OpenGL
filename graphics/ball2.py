from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Ball properties
x1, y1 = 0, 200  # start above floor
r = 30

ty = 0.0         # initial speed
g = -0.5         # gravity
energy_loss = 0.7
min_velocity = 0.5
is_resting = False

floor_y = 50

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)

def draw():
    global x1, y1, r
    glClear(GL_COLOR_BUFFER_BIT)

    # Floor
    glColor3f(0.6,0.6,0.6)
    glBegin(GL_LINES)
    glVertex2f(-250,floor_y)
    glVertex2f(250,floor_y)
    glEnd()

    # Ball
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x1,y1)
    for i in range(0,361):
        angle = math.radians(i)
        glVertex2f(x1 + r*math.cos(angle), y1 + r*math.sin(angle))
    glEnd()
    glFlush()

def translate(value):
    global y1, ty, g, is_resting

    if not is_resting:
        ty += g           # apply gravity
        y1 += ty          # update position

        # Bounce
        if y1 - r <= floor_y:
            y1 = floor_y + r
            ty = -ty * energy_loss

            if abs(ty) < min_velocity:
                ty = 0
                is_resting = True

    glutPostRedisplay()
    glutTimerFunc(30, translate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Bouncing Ball Visible Motion")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(30, translate, 0)
    glutMainLoop()

main()
