
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x1,y1=map(float,input(f"Enter the coordinates of the point:").split())
x2,y2=map(float,input(f"Enter the coordinates of the point:").split())
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,1)
  glLineWidth(2)
  glBegin(GL_LINES)
  glVertex2f(x1,y1)
  glVertex2f(x2,y2)
  glEnd()
  glFlush()
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'Point')
  glutDisplayFunc(draw)
  init()
  glutMainLoop()
main()  

