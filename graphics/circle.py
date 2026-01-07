import math
import time
from OpenGL import * 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Take input from user
x_center = 0
y_center = 230
r=8
def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)
def ploat():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(225/255,78/255,31/255)
	glLineWidth(2)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,361,1):
		glVertex2f(r*math.cos(math.pi*i/180),r*math.sin(math.pi*i/180))
	glEnd()
	glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow(b'SAMPLE')
	glutDisplayFunc(lambda:ploat())
	init()
	glutMainLoop()
main()
