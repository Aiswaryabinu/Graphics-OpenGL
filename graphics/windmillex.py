from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
n=int(input("Enter the number of vertices:"))
points=[]
angle=0
speed=1
for i in range(0,n):
  x,y=map(float,input("Enter the coordinates : ").split())
  points.append((x,y))
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glBegin(GL_POLYGON)
  for i in points:
    glVertex2fv(i)
  glEnd()
  glFlush()
def display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glBegin(GL_LINES)
  glVertex2f(1,0)
  glVertex2f(1,-200)
  glEnd()
  glPushMatrix()
  glTranslatef(1,1,0)
  glRotatef(angle,0,0,1)
  
  for i in range(3):
    draw()
    glRotatef(360/3,0,0,1)

  glPopMatrix()
  glFlush()
def animate(value):
    global angle,speed
    angle+=speed
    if angle>=360:
      angle=0
    glutPostRedisplay()
    glutTimerFunc(60,animate,0)  


def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'windmill')
  glutDisplayFunc(display)
  glutTimerFunc(60,animate,0)  
  init()
  glutMainLoop()
main()  