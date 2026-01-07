from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, math

num_petals = 12
center_radius = 30
petal_radius = 20
# Distance from flower center to petal center: slightly less than center_radius
petal_distance = center_radius * 1.6

petal_colors = [
    (1, 0.3, 0),    # orange
    (1, 0.5, 0.1),
    (1, 0.4, 0.2),
    (1, 0.6, 0.0),
    (1, 0.3, 0.1),
    (1, 0.4, 0.0),
    (1, 0.5, 0.2),
    (1, 0.6, 0.1),
    (1, 0.5, 0.2)
]

current_petal = 0

def draw_circle(cx, cy, r, color):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
    glEnd()

def draw():
    global current_petal
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw center circle (flower core)
    draw_circle(0, 0, center_radius, (0.0, 0.1, 0.5))  # dark blue core

    # Draw petals (heavily overlapping circles)
    for i in range(current_petal):
        angle = math.radians(360 * i / num_petals)
        px = petal_distance * math.cos(angle)
        py = petal_distance * math.sin(angle)
        color = petal_colors[i % len(petal_colors)]
        draw_circle(px, py, petal_radius, color)

    glutSwapBuffers()

def animate(value):
    global current_petal
    if current_petal < num_petals:
        current_petal += 1
    else:
        current_petal = 0
    glutPostRedisplay()
    glutTimerFunc(500, animate, 0)

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-120, 120, -120, 120)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(450, 450)
    glutCreateWindow(b"Overlapping Circle Flower Animation")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()