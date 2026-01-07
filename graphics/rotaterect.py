from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Rectangle parameters
rect_width = 50
rect_height = 50

# Initial position
x = -250  # start from left
y = 0
angle = 0

# Speed
dx = 2       # horizontal movement
rotation_speed = 5

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)

def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex2f(-rect_width/2, -rect_height/2)
    glVertex2f(rect_width/2, -rect_height/2)
    glVertex2f(rect_width/2, rect_height/2)
    glVertex2f(-rect_width/2, rect_height/2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)

    glPushMatrix()
    glTranslatef(x, y, 0)      # Move rectangle to current position
    glRotatef(angle, 0, 0, 1)  # Rotate around center
    draw_rectangle()
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global x, angle
    x += dx                 # Move horizontally
    if x > 300:             # Reset to left after moving off-screen
        x = -300

    angle += rotation_speed # Rotate
    if angle >= 360:
        angle -= 360

    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(200,100)
    glutCreateWindow(b"Rotating Rectangle Moving Horizontally")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()
