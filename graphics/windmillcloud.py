from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
r=30
x=0
y=0
angle=0
tx=1
speed=5
def init():
  glClearColor(1,1,1,0)
  gluOrtho2D(-300,300,-300,300)

def circle():
  glColor3f(1,0,1)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(r*math.cos(i*math.pi/180),r*math.sin(i*math.pi/180))
  glEnd()
def triangle():
  glColor3f(1.5,1,0)
  glBegin(GL_TRIANGLES)
  glVertex2f(0,0)
  glVertex2f(20,100)
  glVertex2f(-20,100)
  glEnd()
  glBegin(GL_TRIANGLES)
  glVertex2f(0,0)
  glVertex2f(20,-100)
  glVertex2f(-20,-100)
  glEnd()
  glBegin(GL_TRIANGLES)
  glVertex2f(0,0)
  glVertex2f(100,20)
  glVertex2f(100,-20)
  glEnd()
  glBegin(GL_TRIANGLES)
  glVertex2f(0,0)
  glVertex2f(-100,20)
  glVertex2f(-100,-20)
  glEnd()

def cloud():
  glColor3f(0.5,0.5,0.5)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(50+50*math.cos(i*math.pi/180),190+50*math.sin(i*math.pi/180))
  glEnd()
def cloud1():
  glColor3f(0.5,0.5,0.5)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(100+20*math.cos(i*math.pi/180),170+20*math.sin(i*math.pi/180))
  glEnd()
def cloud2():
  glColor3f(0.5,0.5,0.5)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(-10+30*math.cos(i*math.pi/180),180+30*math.sin(i*math.pi/180))
  glEnd()    

def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1,0,0)
  glBegin(GL_POLYGON)
  glVertex2f(10,-500)
  glVertex2f(-10,-500)
  glVertex2f(-10,0)
  glVertex2f(10,0)
  glEnd()
  glPushMatrix()
  glTranslatef(x+tx,0,0)
  cloud()
  cloud1()
  cloud2()
  glPopMatrix()
  glPushMatrix()
  glRotatef(angle,0,0,1)
  circle()
  triangle()
  glPopMatrix()
  glFlush()
def animate(value):
  global angle,tx,x,speed
  angle+=speed
  if angle>=360:
    angle=0
  x+=tx
  if x==300:
    x=-300  
  if x>=-120 :
    angle+=15

  glutPostRedisplay()
  glutTimerFunc(30,animate,0)  

  


def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'Point')
  glutDisplayFunc(draw)
  glutTimerFunc(30,animate,0) 
  init()
  glutMainLoop()
main()    