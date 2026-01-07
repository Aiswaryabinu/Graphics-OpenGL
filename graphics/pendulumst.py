from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x,y=map(float,input("Enter x,y (pivot): ").split())
r=int(input("Enter the raduis: "))
angle=0
speed=3
direction=-1
length=120
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0,1,0)
  x_bob=x+length*math.sin(math.radians(angle))
  y_bob=y-length*math.cos(math.radians(angle))
  glBegin(GL_LINES)
  glVertex2f(x,y)
  glVertex2f(x_bob,y_bob)
  glEnd()
  glBegin(GL_TRIANGLE_FAN)
  glVertex2f(x_bob,y_bob)
  for i in range(0,361,1):
    glVertex2f(x_bob+r*math.cos(math.pi*i/180),y_bob+r*math.sin(math.pi*i/180))
  glEnd()
  glFlush()
def animate(value):
  global angle,speed,direction
  angle+=direction*speed
  if angle>60:
    direction=-1
  elif angle<-60:
    direction=1
  glutPostRedisplay()
  glutTimerFunc(60,animate,0)    

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'pendulum')
  glutDisplayFunc(draw)
  glutTimerFunc(60,animate,0)    
  init()
  glutMainLoop()
main()  
