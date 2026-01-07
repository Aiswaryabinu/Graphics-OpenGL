from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Initial position
x1, y1 = map(float, input("Enter the coordinates: ").split())

# Triangle size
size = 20  

# Scaling variables
scale = 0.5
increasing = True

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)

def draw():
    # Draw a triangle centered at (x1, y1)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, 200)        # Top vertex
    glVertex2f(x1 - size, 100) # Bottom left
    glVertex2f(x1 + size, 100) # Bottom right
    glEnd()
    glFlush()

def animate():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glPushMatrix()
    glTranslatef(x1, y1, 0)
    glScalef(scale, scale, 1)
    glTranslatef(-x1, -y1, 0)
    draw()
    glPopMatrix()

def update(value):
    global increasing, scale, x1
    speed = 2
    x1 += speed

    # Move left to right continuously
    if x1 > 300:
        x1 = -300

    # Scaling logic
    if increasing:
        scale += 0.02
        if scale >= 2:
            increasing = False
    else:
        scale -= 0.02
        if scale <= 0.5:
            increasing = True

    glutPostRedisplay()
    glutTimerFunc(60, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b'Scaling Triangle Animation')
    glutDisplayFunc(animate)
    glutTimerFunc(60, update, 0)
    init()
    glutMainLoop()

main()
