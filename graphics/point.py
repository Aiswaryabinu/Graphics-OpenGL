from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x1,y1=map(float,input(f"Enter the coordinates of the point:").split())

def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,1)
  glLineWidth(5)
  glBegin(GL_POINTS)
  glVertex2f(x1,y1)
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