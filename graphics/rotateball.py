from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x1, y1 = map(float, input("Enter the center coordinates: ").split())
r = int(input("Enter the radius: "))
angle=0
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glLineWidth(3)
  glBegin(GL_LINES)
  glVertex(-300,50)
  glVertex(300,50)
  glEnd()
  glBegin(GL_TRIANGLE_FAN)
  glVertex2f(x1,y1)
  for i in range(0,361,1):
    glVertex2f(x1+r*math.cos(math.pi*i/180),y1+r*math.sin(math.pi*i/180))
  glEnd()
  glFlush()  
def translate(value):
  global x1,tx,angle
  tx=2
  x1+=tx
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