from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=10
y=190
r=30
tx=2
ty=2
angle=0
wheel_angle=0
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def circle():
  glColor3f(1,0,0)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(r*math.cos(math.pi*i/180),r*math.sin(math.pi*i/180))
  glEnd()
def spoke():
  glColor3f(1,1,0)
  glBegin(GL_LINES)
  for i in range(6):
    theta=math.radians(wheel_angle+i*60)
    glVertex2f(x,y)
    glVertex2f(x+30*math.cos(theta),y+30*math.sin(theta))
  glEnd()  
def line():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0,1,0)
   glBegin(GL_LINES)
   glVertex2f(0,190)
   glVertex2f(30,30)
   glEnd()
   glBegin(GL_LINES)
   glVertex2f(30,30)
   glVertex2f(80,30)
   glEnd()
   glBegin(GL_LINES)
   glVertex2f(80,30)
   glVertex2f(90,190)
   glEnd()
   circle()
   glPushMatrix()
   glRotatef(wheel_angle,0,0,1)
   spoke()
   glPopMatrix()
   glFlush()


def animate(value):
    global tx, ty, x, y, wheel_angle
    x += tx
    y -= ty
    if x == 30 or y == 30:   # Reset when ball reaches pit (adjust as needed)
        y = 30
        x+=tx
    if x==80:
       x+=tx
       y+=ty   
    wheel_angle += 2
    if wheel_angle >= 360:
        wheel_angle = 0
       

    glutPostRedisplay()
    glutTimerFunc(40, animate, 0)



def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,100)
  glutCreateWindow(b'pit')
  glutDisplayFunc(line)
  glutTimerFunc(40,animate,0)
  init()
  glutMainLoop()
main()      