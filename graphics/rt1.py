from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x1, y1 = map(float, input("Enter the center coordinates: ").split())
r = int(input("Enter the radius: "))
angle=0
speed=2
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glLineWidth(3)
  glPushMatrix()
  glRotate(angle,0,0,1)
  glBegin(GL_POLYGON)
  glVertex2f(x1,200)
  glVertex2f(x1-10,100)
  glVertex2f(x1+10,100)
  glEnd()
  glPopMatrix()
  glFlush()  
def translate(value):
  global x1,tx,angle
  tx=2
  x1+=tx
  if tx>300:
    x1=300
  angle += 5
  if angle >= 360:
      angle -= 360

  glutPostRedisplay()
  glutTimerFunc(30,translate,0)    
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'ROtate ball')
  glutDisplayFunc(draw)
  init()
  glutTimerFunc(30,translate,0)
  glutMainLoop()
main()    