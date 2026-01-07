from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
n=int(input("Enter the number of vertices :"))
points=[]
for i in range(0,n):
  x,y=map(float,input("Enter the x,y :").split())
  points.append((x,y))
angle=0
speed=0.5
target_speed=5  
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  
  glBegin(GL_POLYGON)
  for item in points:
    glVertex2fv(item)
  glEnd()
  glFlush()
def display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glPushMatrix()
  glTranslatef(0,0,0)
  glRotatef(angle,0,0,1)
  for i in range(4):
    draw()
    glRotatef(360/4,0,0,1)
  glPopMatrix()  
def update(value):
  global angle,speed,target_speed
  if speed<target_speed:
    speed+=0.1
  elif speed>target_speed:
    speed+=0.1
  angle+=speed
  if angle>=360:
    angle=0
  glutPostRedisplay()
  glutTimerFunc(30, update, 0)      




def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'windmill')
  glutDisplayFunc(display)
  glutTimerFunc(30, update, 0) 
  init()
  glutMainLoop()
main()    