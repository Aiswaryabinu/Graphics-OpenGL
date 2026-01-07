from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x1,y1=map(float,input("Enter the coordinates: ").split())
r=int(input("Entre the raduis: "))
scale=0.5
increasing=True
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def draw():
  glBegin(GL_TRIANGLE_FAN)
  glVertex2f(x1,y1)
  for i in range(0,361):
      glVertex2f(x1+r*math.cos(math.pi*i/180),y1+r*math.sin(math.pi*i/180))
  glEnd()
  glFlush()
def animate():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1,0,0)
   glPushMatrix()
   glTranslatef(x1,y1,0)
   glScalef(scale,scale,1)
   glTranslatef(-x1,-y1,0)
   draw()
   glPopMatrix()
def update(value):
   global increasing,scale,tx,x1
   tx=2
   x1+=2
   if x1>300:
      x1=-300
   if increasing:
      scale+=0.2
      if scale>=2:
         increasing=False
   else:
      scale-=0.2
      if scale<=0.5:
         increasing=True
   glutPostRedisplay()
   glutTimerFunc(60,update,0)     
                

   

def main():
   glutInit()
   glutInitDisplayMode(GLUT_RGBA)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(600,0)
   glutCreateWindow(b'shrinking ball')
   glutDisplayFunc(animate)
   glutTimerFunc(60,update,0) 
   init()
   glutMainLoop()
main()   

