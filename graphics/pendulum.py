import math, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Pendulum parameters
pivot_x, pivot_y = 0, 200   # Pivot point (top)
length = 150                # Length of string
radius = 20                 # Bob radius
angle = 30                  # Initial angle (degrees)
direction = -1              # Swing direction (-1 = left, 1 = right)
speed = 1.0                 # Angle step per frame

def init():
    glClearColor(0, 0, 0, 1)    # Background black
    gluOrtho2D(-300, 300, -300, 300)

def draw_circle(x, y, r):
    """Draw a circle for bob"""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(361):
        glVertex2f(x + r * math.cos(math.radians(i)), y + r * math.sin(math.radians(i)))
    glEnd()

def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)  # White

    # Compute bob position using angle
    bob_x = pivot_x + length * math.sin(math.radians(angle))
    bob_y = pivot_y - length * math.cos(math.radians(angle))

    # Draw pendulum string
    glBegin(GL_LINES)
    glVertex2f(pivot_x, pivot_y)
    glVertex2f(bob_x, bob_y)
    glEnd()

    # Draw pendulum bob
    glColor3f(1, 0, 0)  # Red
    draw_circle(bob_x, bob_y, radius)

    glFlush()

def update(value):
    global angle, direction

    # Update angle
    angle += direction * speed
    if angle > 60:   # Max swing right
        direction = -1
    elif angle < -60: # Max swing left
        direction = 1

    glutPostRedisplay()                # Redraw scene
    glutTimerFunc(16, update, 0)       # Call again after ~16ms (~60fps)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Animated Pendulum")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)  # Start animation
    glutMainLoop()

main()
