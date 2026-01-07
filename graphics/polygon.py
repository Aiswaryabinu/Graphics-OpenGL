from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys 
import math
n=int(input(f"Enter the number of vertices:"))
points=[]
for i in range(0,n):
  x,y=map(float,input(f"Enter the coordinates of point {i+1}:").split())
  points.append((x,y))
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,1)
  glLineWidth(2)
  glBegin(GL_POLYGON)
  for i in points:
    glVertex2fv(i)
  glEnd()
  glFlush()
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'Polygon')
  glutDisplayFunc(draw)
  init()
  glutMainLoop()
main()      
     
   