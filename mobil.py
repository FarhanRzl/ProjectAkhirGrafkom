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
    glColor(0,25,160,215)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle2(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor(0,25,160,215)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle3(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor(204, 204, 0)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()

def circle4(cx,cy,r,num_segment):
    glBegin(GL_POLYGON)
    glColor(204, 204, 0)
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

#sisi kiri luar
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    #bagian bumper depan 
    glVertex2f(-533,-143)
    glVertex2f(-563,-77)
    #bagian kap mesin
    glVertex2f(-519,93)
    glVertex2f(-321,128)
    #roof
    glVertex2f(-154,289)
    glVertex2f(316,289)
    #kaca belakang & body belakang
    glVertex2f(423,121)
    glVertex2f(438,-81)
    #bumper belakang
    glVertex2f(415,-144)
    glEnd()

#kaca
    glColor3ub(204, 204, 0)
    glBegin(GL_POLYGON)
    #kaca depan
    glVertex2f(-294,128)
    glVertex2f(-152,271)
    glVertex2f(-49,271)
    glVertex2f(-49,128)
    glEnd()
    #kaca tengah
    glBegin(GL_POLYGON)
    glVertex2f(-28,128)
    glVertex2f(-28,271)
    glVertex2f(164,271)
    glVertex2f(164,128)
    glEnd()
    #kaca belakang
    glBegin(GL_POLYGON)
    glVertex2f(185,128)
    glVertex2f(185,271)
    glVertex2f(313,271)
    glVertex2f(395,128)
    # #kaca belakang & body belakang
    # glVertex2f(164,132)
    # #bumper belakang
    # glVertex2f(185,126)
    # glVertex2f(3.5,129)
    glEnd()


# #sisi tengah bawah luar
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)
#     glVertex2f(200,-170)
#     glVertex2f(200,-240)

#     glVertex2f(-200,-240)
#     glVertex2f(-200,-170)
#     glEnd()

# #sisi kanan luar
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)
#     glVertex2f(200,-170)
#     glVertex2f(200, 90)

#     glVertex2f(520,90)
#     glVertex2f(470,-170)
#     glEnd()

# #sisi tengah atas luar
#     glColor3ub(255, 255, 255)
#     glBegin(GL_POLYGON)
#     glVertex2f(-200,170)
#     glVertex2f(200,170)

#     glVertex2f(200,-240)
#     glVertex2f(-200,-170)
#     glEnd()

# #sisi kiri
#     glColor3ub(204, 204, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(-140,-110)
#     glVertex2f(-460,-110)

#     glVertex2f(-410,30)
#     glVertex2f(-140,30)
#     glEnd()

# #sisi tengah bawah
#     glColor3ub(204, 204, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(140,-110)
#     glVertex2f(140,-180)

#     glVertex2f(-140,-180)
#     glVertex2f(-140,-110)
#     glEnd()

# #sisi kanan
#     glColor3ub(204, 204, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(140,-110)
#     glVertex2f(140, 30)

#     glVertex2f(460,30)
#     glVertex2f(410,-110)
#     glEnd()

# #sisi tengah atas
#     glColor3ub(204, 204, 0)
#     glBegin(GL_POLYGON)
#     glVertex2f(-140,110)
#     glVertex2f(140,110)

#     glVertex2f(140,-180)
#     glVertex2f(-140,-110)
#     glEnd()


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
    circle1(-300,-120,100,360)
    circle2(200,-120,100,360)
    circle3(-300,-120,60,360)
    circle4(200,-120,60,360)
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