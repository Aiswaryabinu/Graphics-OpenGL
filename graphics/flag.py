from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x,y=map(float,input("Enter the coordinates: ").split())
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glLineWidth(3)
  glBegin(GL_LINES)
  glVertex2f(50,200)
  glVertex2f(50,-50)
  glEnd()
  glBegin(GL_QUADS)
  glVertex2f(x,y)
  glVertex2f(x+120,y)
  glVertex2f(x+120,y+80)
  glVertex2f(x,y+80)
  glEnd()
  glFlush()
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'flag')
  glutDisplayFunc(draw)
  init()
  glutMainLoop()
main()      