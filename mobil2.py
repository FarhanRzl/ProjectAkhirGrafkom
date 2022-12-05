from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
w,h= 1000,1000
posisiX=0
posisiY=0

posisiXscale=1
posisiYscale=1

posisiXrotate=0
def circle1(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor3ub(96,96,96)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle2(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor3ub(96,96,96)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle3(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle4(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def square():
    glTranslated(posisiX,posisiY,0)
    glScaled(posisiXscale,posisiYscale,0)
    glRotated(posisiXrotate,0,0,1)

#body
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    #body depan
    glVertex2f(216,-49)#(P)
    glVertex2f(277,-43)#(Q)
    glVertex2f(299,-28)#(R)
    glVertex2f(292,-21)#(S)
    glVertex2f(298,-11)#(T)
    glVertex2f(300,10)#(U)
    glVertex2f(288,18)#(v)
    glVertex2f(280,36)#(w)
    #body tengah
    glVertex2f(208,57)#(L)
    glVertex2f(126,67)#(z)
    glVertex2f(19,115)#(m)
    glVertex2f(-33,119)#(v1)
    glVertex2f(-88,117)#(k)
    glVertex2f(-154,107)#(j)
    glVertex2f(-273,68)#(i)
    #body belakang
    glVertex2f(-312,65)#(h)
    glVertex2f(-320,20)#(g)
    glVertex2f(-329,20)#(f)
    glVertex2f(-329,-9)#(c)
    glVertex2f(-298,-37)#(d)
    glVertex2f(-257,-46)#(e)
    glVertex2f(-174,-46)#(n)
    glEnd()
#lampu depan
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(288,18)#(v)
    glVertex2f(244,19)#(o1)
    glVertex2f(224,40)#(p1)
    glVertex2f(280,36)#(w)
    glEnd()
#lampu belakang
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-312,65)#(H)
    glVertex2f(-281,47)#(Q1)
    glVertex2f(-320,20)#(G)
    glEnd()
#kaca depan
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(107,61)
    glVertex2f(18,106)#(H)
    glVertex2f(25,112)#(Q1)
    glVertex2f(126,67)
    glEnd()
#kaca1
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-36,59)#(L)
    glVertex2f(-43,105)#()
    glVertex2f(3,100)#()
    glVertex2f(44,84)#()
    glVertex2f(90,54)#(j1)
    glEnd()
#pintu1
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-35,-29)#()
    glVertex2f(105,-30)#(g1)
    glVertex2f(107,36)#(s1)
    glVertex2f(90,54)#(j1)
    glVertex2f(-36,59)
    glEnd()
#kaca2
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-199,65)#(h1)
    glVertex2f(-173,85)#(t1)
    glVertex2f(-140,100)#(e1)
    glVertex2f(-107,105)#(f1)
    glVertex2f(-65,107)#()
    glVertex2f(-60,62)#(m)
    glEnd()
#pintu2
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-133,-31)#()
    glVertex2f(-141,-14)#(g1)
    glVertex2f(-149,1)#(s1)
    glVertex2f(-160,20)
    glVertex2f(-174,32)#(j1)
    glVertex2f(-198,45)
    glVertex2f(-199,65)
    glVertex2f(-60,62)
    glVertex2f(-57,-30)
    glEnd()

def gerak(key,x ,y ):
    global posisiX
    global posisiY
    global posisiXscale
    global posisiYscale
    if key == GLUT_KEY_RIGHT:
        posisiX += 100
    elif key == GLUT_KEY_LEFT:
        posisiX -= 100
    elif key == GLUT_KEY_UP:
        posisiY += 100
    elif key == GLUT_KEY_DOWN:
        posisiY -= 100
    elif key == GLUT_KEY_PAGE_UP:
        posisiXscale += 0.1
        posisiYscale += 0.1
    elif key == GLUT_KEY_PAGE_DOWN:
        if posisiXscale < 0.2 and posisiYscale < 0.2:
            posisiXscale -= 0
            posisiYscale -= 0
        else:
            posisiXscale -= 0.1
            posisiYscale -= 0.1

def rotated(button,state,x,y):
    global posisiXrotate
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        posisiXrotate += 10
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        posisiXrotate -= 10

# def tes(key, x, y):
#     global posisiXrotate
#     if key == chr(32):
#         posisiXrotate += 10


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-w, w, -h, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    circle1(-200,-30,50,360)
    circle2(150,-30,50,360)
    circle3(-200,-30,30,360)
    circle4(150,-30,30,360)
    # square2()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutSpecialFunc(gerak)
glutMouseFunc(rotated)
# glutKeyboardFunc(tes)
glutIdleFunc(showScreen)
glutMainLoop()