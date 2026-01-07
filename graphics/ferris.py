from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
wheel_angle=0
x=0
y=0
angle=0
l_angle=0
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def circle(x,y):
  glColor3f(1,0,0)
  glBegin(GL_LINE_LOOP)
  for i in range(0,361):
    glVertex2f(x+190*math.cos(i*math.pi/180),y+190*math.sin(i*math.pi/180))
  glEnd()
def spoke():
  glColor3f(1,1,0)
  glBegin(GL_LINES)
  for i in range(6):
    theta=math.radians(wheel_angle+i*60)
    glVertex2f(x,y)
    glVertex2f(x+190*math.cos(theta),y+190*math.sin(theta))
  glEnd()


def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  circle(0,0)

  glPushMatrix()
  glRotatef(angle,0,0,1)
  spoke()
  glPopMatrix()
  radius = 190  # distance from wheel center
  seat_size = 40

  for i in range(6):  # 6 seats at each spoke
    theta = math.radians(angle + i*60)
    seat_x = radius * math.cos(theta)-seat_size/2
    seat_y = radius * math.sin(theta)-seat_size/2
    square(seat_x, seat_y)

  glFlush()

  
def update(value):
  global angle
  angle+=1
  if angle>=360:
    angle=0
  
  glutPostRedisplay()
  glutTimerFunc(40,update,0)  



def square(a,b):
  glColor3f(0,1,0)
  glBegin(GL_LINE_LOOP)
  glVertex2f(a,b)
  glVertex2f(a+60,b)
  glVertex2f(a+60,b+60)
  glVertex2f(a,b+60)   
  glEnd()

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'ferris')
  glutDisplayFunc(draw)
  glutTimerFunc(40,update,0)  

  init()
  glutMainLoop()
main()  
  

