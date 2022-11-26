from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os
os.system('cls')

w,h= 1280,720

jedag, jedug = 1,1
x = 50
cek_x = 50
cek_point = 30
kecepatan = 1
pos_x_awan = 20
pos_y_awan = 0
pos_x_gjalan = 0
pos_y_gjalan = 0
pos_x_gkota1 = 0
pos_y_gkota1 = 0

pos_x_mobil = 300
pos_y_mobil = -260

def MainMenu():
    global jedag,jedug
    #M
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP)
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(3.576757916323,5.5896610088214)
    glVertex2f(4.0130331519056,5.5896610088214)
    glVertex2f(4.3869833538336,4.8417606049654)
    glVertex2f(4.7609335557616,5.5896610088214)
    glVertex2f(5.2387588137807,5.5896610088214)
    glVertex2f(5.0102336903803,4.5509104479103)
    glVertex2f(5.1972087913443,4.0107601562365)
    glVertex2f(4.5947334660158,4.0107601562365)
    glVertex2f(4.6570584996705,4.6340104927832)#1
    glVertex2f(4.2623332865243,4.1977352572005)
    glVertex2f(3.950708118251,4.8002105825289)
    glVertex2f(3.7221829948505,3.9899851450183)
    glVertex2f(3.2235827256132,4.0107601562365)
    glVertex2f(3.5975329275412,4.8002105825289)
    glEnd()

def langit():
    #LANGIT
    glColor3ub(135, 206, 235)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 720)
    glVertex2f(1280, 720)
    glVertex2f(1280, 0)
    glEnd()

def Jalan():
    #JALAN
    glColor3ub(105, 105, 105)
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(1280, 210)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()

    #RUMPUT
    #TENGAH
    # glColor3ub(50, 205, 50)
    # glBegin(GL_QUADS)
    # glVertex2f(0, 120)
    # glVertex2f(1280, 120)
    # glVertex2f(1280, 100)
    # glVertex2f(0, 100)
    # glEnd()
    #ATAS
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 220)
    glVertex2f(1280, 220)
    glVertex2f(1280, 200)
    glVertex2f(0, 200)
    glEnd()
    #BAWAH
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 20)
    glVertex2f(1280, 20)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()

def kota1():
    glTranslated(pos_x_gkota1,pos_y_gkota1,0)
    #gedung 1
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(0, 400)
    glVertex2f(150, 400)
    glVertex2f(150, 210)

    glVertex2f(70, 400)
    glVertex2f(100, 430)
    glVertex2f(140, 430)
    glVertex2f(140, 400)
    glEnd()

    #gedung 2
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(150, 210)
    glVertex2f(150, 340)
    glVertex2f(280, 340)
    glVertex2f(280, 210)
    glEnd()

    #gedung 3
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(300, 210)
    glVertex2f(300, 500)
    glVertex2f(500, 500)
    glVertex2f(500, 210)

    glVertex2f(320, 500)
    glVertex2f(320, 550)
    glVertex2f(370, 550)
    glVertex2f(370, 500)

    glVertex2f(370, 500)
    glVertex2f(370, 518)
    glVertex2f(400, 518)
    glVertex2f(400, 500)
    glEnd()

    #gedung 4
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(500, 210)
    glVertex2f(500, 380)
    glVertex2f(600, 380)
    glVertex2f(600, 210)
    glEnd()  

    #gedung 5
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(600, 210)
    glVertex2f(600, 450)
    glVertex2f(730, 450)
    glVertex2f(730, 210)
    glEnd() 

    #gedung 6
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(780, 210)
    glVertex2f(780, 260)
    glVertex2f(880, 260)
    glVertex2f(880, 210)

    glVertex2f(760, 260)
    glVertex2f(780, 300)
    glVertex2f(880, 300)
    glVertex2f(900, 260)
    glEnd() 

    #gedung 7
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(900, 210)
    glVertex2f(900, 400)
    glVertex2f(1020, 400)
    glVertex2f(1020, 210)
    glEnd()

    #gedung 8
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1040, 210)
    glVertex2f(1040, 450)
    glVertex2f(1150, 450)
    glVertex2f(1150, 210)
    glEnd()

    #gedung 9
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1200, 210)
    glVertex2f(1200, 400)
    glVertex2f(1320, 400)
    glVertex2f(1320, 210)
    glEnd()

    #gedung 10
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1350, 210)
    glVertex2f(1350, 500)
    glVertex2f(1500, 500)
    glVertex2f(1500, 210)
    glEnd()

    #gedung 11
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1550, 210)
    glVertex2f(1550, 550)
    glVertex2f(1750, 550)
    glVertex2f(1750, 210)
    glEnd()

    #gedung 12
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1780, 210)
    glVertex2f(1780, 260)
    glVertex2f(1860, 260)
    glVertex2f(1860, 210)

    glVertex2f(1780, 260)
    glVertex2f(1800, 300)
    glVertex2f(1840, 300)
    glVertex2f(1860, 260)
    glEnd()

    #gedung 13
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1860, 210)
    glVertex2f(1860, 400)
    glVertex2f(2000, 400)
    glVertex2f(2000, 210)
    glEnd()

    #gedung 14
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2020, 210)
    glVertex2f(2020, 500)
    glVertex2f(2200, 500)
    glVertex2f(2200, 210)
    glEnd()

    #gedung 15
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2200, 210)
    glVertex2f(2200, 400)
    glVertex2f(2340, 400)
    glVertex2f(2340, 210)
    glEnd()

    #gedung 0
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(-10, 210)
    glVertex2f(-10, 400)
    glVertex2f(-130, 400)
    glVertex2f(-130, 210)
    glEnd()

def TransKota():
    kota1()
    global pos_x_gkota1, pos_y_gkota1

    # gimana apel bisa jatuh
    pos_x_gkota1 -= kecepatan

    #kalo dah sampe bawah bikin dari atas lagi
    if pos_x_gkota1 < -1135:
        pos_x_gkota1 = 100

def pembatas():
    #PEMBATAS
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-12800, 210)
    glVertex2f(-12800, 225)
    glVertex2f(12800, 225)
    glVertex2f(1280, 210)
    glEnd()
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-12800, 10)
    glVertex2f(-12800, 25)
    glVertex2f(12800, 25)
    glVertex2f(12800, 10)
    glEnd()

def Garis(kx, ky):
    glColor3ub(255, 255, 255)
    glLineWidth(25)
    glBegin(GL_LINES)
    glVertex2f(kx, ky)
    glVertex2f(kx + 170, ky)
    glEnd()

def Awan():
    # global pos_x_awan, pos_y_awan
    # glTranslated(pos_x_awan,pos_y_awan,0)

    # #gimana apel bisa jatuh
    # pos_x_awan -= kecepatan

    # #kalo dah sampe bawah bikin dari atas lagi
    # if pos_x_awan < -650:
    #     pos_x_awan = 600
    #AWAN
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(100, 450)
    glVertex2f(200, 450)
    glVertex2f(200, 500)
    glVertex2f(100, 500)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(240, 600)
    glVertex2f(280, 600)
    glVertex2f(280, 580)
    glVertex2f(240, 580)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(500, 550)
    glVertex2f(650, 550)
    glVertex2f(650, 500)
    glVertex2f(500, 500)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(850, 600)
    glVertex2f(1050, 600)
    glVertex2f(1050, 550)
    glVertex2f(850, 550)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(950, 450)
    glVertex2f(1000, 450)
    glVertex2f(1000, 400)
    glVertex2f(950, 400)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1060, 550)
    glVertex2f(1120, 550)
    glVertex2f(1120, 520)
    glVertex2f(1060, 520)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1160, 450)
    glVertex2f(1220, 450)
    glVertex2f(1220, 420)
    glVertex2f(1160, 420)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(800, 400)
    glVertex2f(860, 400)
    glVertex2f(860, 370)
    glVertex2f(800, 370)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(380, 400)
    glVertex2f(450, 400)
    glVertex2f(450, 370)
    glVertex2f(380, 370)
    glEnd()

def mobil():
    global pos_x_mobil, pos_y_mobil
    glTranslated(pos_x_mobil, pos_y_mobil, 0)
    glColor3ub(255, 213, 0)
    # pos_x_mobil = 500
    # pos_y_mobil = -180
    # pos_x_mobil = 800
    # pos_y_mobil = -320
    # pos_x_mobil = 300
    # pos_y_mobil = -260
    #Badan atas
    glBegin(GL_POLYGON)
    glVertex2f(52 , 366)#c17
    glVertex2f(52 , 371)
    glVertex2f(52 , 375)
    glVertex2f(54 , 376)
    glVertex2f(55 , 377)
    glVertex2f(57 , 382)
    glVertex2f(58 , 384)
    glVertex2f(59 , 385)
    glVertex2f(78 , 392)
    glVertex2f(81 , 395)
    glVertex2f(112 , 408)
    glVertex2f(114 , 410)
    glVertex2f(118 , 411)
    glVertex2f(124 , 412)
    glVertex2f(150 , 413)
    glVertex2f(155 , 413)
    glVertex2f(182 , 412)
    glVertex2f(184 , 411)
    glVertex2f(186 , 410)
    glVertex2f(187 , 408)
    glVertex2f(196 , 393)
    glVertex2f(196 , 392)
    glVertex2f(196 , 388)
    glVertex2f(197 , 384)
    glVertex2f(199 , 383)
    glVertex2f(200 , 380)
    glVertex2f(200 , 378)
    glVertex2f(201 , 377)
    glVertex2f(202 , 376)
    glVertex2f(202 , 365)
    glEnd()
    #Badan bawah
    glColor3ub(255, 213, 0)
    glBegin(GL_POLYGON)
    glVertex2f(52 , 366)#c17
    glVertex2f(53 , 363)
    glVertex2f(54 , 361)
    glVertex2f(55 , 359)
    glVertex2f(64 , 359)
    glVertex2f(64 , 361)
    glVertex2f(65 , 363)
    glVertex2f(66 , 367)
    glVertex2f(67 , 370)
    glVertex2f(70 , 373)
    glVertex2f(72 , 374)
    glVertex2f(74 , 375)
    glVertex2f(77 , 375)
    glVertex2f(80 , 375)
    glVertex2f(83 , 374)
    glVertex2f(86 , 372)
    glVertex2f(88 , 370)
    glVertex2f(89 , 367)
    glVertex2f(90 , 364)
    glVertex2f(90 , 362)
    glVertex2f(91 , 360)
    glVertex2f(91 , 357)
    glVertex2f(167 , 357)
    glVertex2f(167 , 361)
    glVertex2f(167 , 363)
    glVertex2f(168 , 366)
    glVertex2f(168 , 369)
    glVertex2f(171 , 372)
    glVertex2f(173 , 374)
    glVertex2f(176 , 375)
    glVertex2f(178 , 376)
    glVertex2f(181 , 376)
    glVertex2f(183 , 375)
    glVertex2f(185 , 374)
    glVertex2f(188 , 373)
    glVertex2f(190 , 371)
    glVertex2f(191 , 369)
    glVertex2f(192 , 365)
    glVertex2f(193 , 363)
    glVertex2f(193 , 361)
    glVertex2f(194 , 361 )
    glVertex2f(197 , 362)
    glVertex2f(199 , 362)
    glVertex2f(200 , 364)
    glVertex2f(202 , 365)
    glEnd()
    #Roda kanan atas
    glColor3ub(0 , 0 ,0)
    glBegin(GL_POLYGON)
    glVertex2f(64 , 359)
    glVertex2f(64 , 361)
    glVertex2f(65 , 363)
    glVertex2f(66 , 367)
    glVertex2f(67 , 370)
    glVertex2f(70 , 373)
    glVertex2f(72 , 374)
    glVertex2f(74 , 375)
    glVertex2f(77 , 375)
    glVertex2f(80 , 375)
    glVertex2f(83 , 374)
    glVertex2f(86 , 372)
    glVertex2f(88 , 370)
    glVertex2f(89 , 367)
    glVertex2f(90 , 364)
    glVertex2f(90 , 362)
    glVertex2f(91 , 360)
    glVertex2f(91 , 357)
    glEnd()
    #Roda kanan bawah
    glColor3ub(0 , 0 ,0)
    glBegin(GL_POLYGON)
    glVertex2f(64 , 359)
    glVertex2f(65 , 357)
    glVertex2f(66 , 354)
    glVertex2f(69 , 351)
    glVertex2f(71 , 350)
    glVertex2f(73 , 349)
    glVertex2f(75 , 348)
    glVertex2f(80 , 348)
    glVertex2f(82 , 349)
    glVertex2f(84 , 350)
    glVertex2f(86 , 351)
    glVertex2f(88 , 353)
    glVertex2f(90 , 355)
    glVertex2f(91 , 357)
    glEnd()
    #Roda kiri atas
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(167 , 357)
    glVertex2f(167 , 361)
    glVertex2f(167 , 363)
    glVertex2f(168 , 366)
    glVertex2f(168 , 369)
    glVertex2f(171 , 372)
    glVertex2f(173 , 374)
    glVertex2f(176 , 375)
    glVertex2f(178 , 376)
    glVertex2f(181 , 376)
    glVertex2f(183 , 375)
    glVertex2f(185 , 374)
    glVertex2f(188 , 373)
    glVertex2f(190 , 371)
    glVertex2f(191 , 369)
    glVertex2f(192 , 365)
    glVertex2f(193 , 363)
    glVertex2f(193 , 361)
    glEnd()
    #Roda kiri bawah
    glColor3ub(0 , 0 ,0)
    glBegin(GL_POLYGON)
    glVertex2f(167 , 357)
    glVertex2f(168 , 356)
    glVertex2f(169 , 355)
    glVertex2f(172 , 351)
    glVertex2f(174 , 350)
    glVertex2f(175 , 349)
    glVertex2f(177 , 348)
    glVertex2f(183 , 348)
    glVertex2f(185 , 349)
    glVertex2f(187 , 350)
    glVertex2f(190 , 352)
    glVertex2f(191 , 354)
    glVertex2f(192 , 356)
    glVertex2f(193 , 359)
    glVertex2f(193 , 361)
    glEnd()
    #pintu kiri
    glColor3ub(0 , 0 ,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(93 , 374)
    glVertex2f(93 , 378)
    glVertex2f(93 , 383)
    glVertex2f(93 , 389)
    glVertex2f(92 , 388)
    glVertex2f(90 , 389)
    glVertex2f(89 , 389)
    glVertex2f(88 , 390)
    glVertex2f(88 , 391)
    glVertex2f(89 , 392)
    glVertex2f(90 , 393)
    glVertex2f(93 , 395)
    glVertex2f(96 , 397)
    glVertex2f(98 , 398)
    glVertex2f(115 , 406)
    glVertex2f(117 , 407)
    glVertex2f(120 , 408)
    glVertex2f(123 , 409)
    glVertex2f(126 , 410)
    glVertex2f(146 , 410)
    glVertex2f(147 , 409)
    glVertex2f(149 , 407)
    glVertex2f(150 , 404)
    glVertex2f(149 , 376)
    glVertex2f(148 , 373)
    glVertex2f(148 , 369)
    glVertex2f(147 , 366)
    glVertex2f(146 , 364)
    glVertex2f(144 , 363)
    glVertex2f(100 , 363)
    glVertex2f(97 , 364)
    glVertex2f(95 , 366)
    glVertex2f(94 , 369)
    glEnd()
    # Spion
    glColor3ub(0 , 0 ,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(98 , 388)
    glVertex2f(92 , 388)
    glVertex2f(90 , 389)
    glVertex2f(89 , 389)
    glVertex2f(88 , 390)
    glVertex2f(88 , 391)
    glVertex2f(89 , 392)
    glVertex2f(90 , 393)
    glVertex2f(93 , 395)
    glVertex2f(96 , 397)
    glVertex2f(98 , 398)
    glEnd()
    #roda d kiri
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(68 , 360)
    glVertex2f(68 , 362)
    glVertex2f(69 , 364)
    glVertex2f(70 , 367)
    glVertex2f(71 , 369)
    glVertex2f(73 , 370)
    glVertex2f(75 , 371)
    glVertex2f(78 , 372)
    glVertex2f(80 , 371)
    glVertex2f(83 , 370)
    glVertex2f(84 , 369)
    glVertex2f(86 , 366)
    glVertex2f(87 , 365)
    glVertex2f(87 , 362)
    glEnd()
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(68 , 360)
    glVertex2f(69 , 357)
    glVertex2f(71 , 355)
    glVertex2f(73 , 353)
    glVertex2f(74 , 352)
    glVertex2f(77 , 352)
    glVertex2f(80 , 352)
    glVertex2f(81 , 353)
    glVertex2f(84 , 355)
    glVertex2f(85 , 357)
    glVertex2f(87 , 359)
    glVertex2f(87 , 362)
    glEnd()
    # roda d kanan
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(170 , 363)
    glVertex2f(171 , 365)
    glVertex2f(173 , 368)
    glVertex2f(175 , 370)
    glVertex2f(178 , 371)
    glVertex2f(180 , 371)
    glVertex2f(183 , 370)
    glVertex2f(185 , 369)
    glVertex2f(187 , 368)
    glVertex2f(188 , 366)
    glVertex2f(189 , 365)
    glVertex2f(189 , 362)
    glEnd()
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(170 , 363)
    glVertex2f(171 , 360)
    glVertex2f(172 , 358)
    glVertex2f(173 , 356)
    glVertex2f(175 , 354)
    glVertex2f(177 , 353)
    glVertex2f(179 , 352)
    glVertex2f(181 , 352)
    glVertex2f(183 , 353)
    glVertex2f(185 , 355)
    glVertex2f(186 , 356)
    glVertex2f(188 , 359)
    glVertex2f(189 , 362)
    glEnd()
    #kaca kiri
    glColor3ub(255 , 255 , 255)
    glBegin(GL_POLYGON)
    glVertex2f(98 , 388)
    glVertex2f(98 , 396)
    glVertex2f(112 , 403)
    glVertex2f(114 , 404)
    glVertex2f(116 , 405)
    glVertex2f(118 , 406)
    glVertex2f(120 , 406)
    glVertex2f(125 , 408)
    glVertex2f(144 , 408)
    glVertex2f(145 , 407)
    glVertex2f(146 , 406)
    glVertex2f(146 , 404)
    glVertex2f(146 , 391)
    glEnd()
    glColor3ub(255 , 255 , 255)
    glBegin(GL_POLYGON)
    glVertex2f(146 , 390)
    glVertex2f(145 , 389)
    glVertex2f(98 , 388)
    glEnd()
    glColor3ub(0 , 0 ,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(98 , 388)
    glVertex2f(98 , 396)
    glVertex2f(112 , 403)
    glVertex2f(114 , 404)
    glVertex2f(116 , 405)
    glVertex2f(118 , 406)
    glVertex2f(120 , 406)
    glVertex2f(125 , 408)
    glVertex2f(144 , 408)
    glVertex2f(145 , 407)
    glVertex2f(146 , 406)
    glVertex2f(146 , 404)
    glVertex2f(146 , 391)
    glVertex2f(146 , 390)
    glVertex2f(145 , 389)
    glEnd()
    # kaca kanan
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(152 , 391)
    glVertex2f(152 , 406)
    glVertex2f(152 , 407)
    glVertex2f(152 , 408)
    glVertex2f(177 , 407)
    glVertex2f(178 , 406)
    glVertex2f(179 , 405)
    glVertex2f(180 , 404)
    glVertex2f(181 , 402)
    glVertex2f(185 , 396)
    glVertex2f(185 , 394)
    glVertex2f(186 , 393)
    glVertex2f(186 , 392)
    glVertex2f(184 , 392)
    glVertex2f(182 , 391)
    glEnd()
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(152 , 391)
    glVertex2f(152 , 406)
    glVertex2f(152 , 407)
    glVertex2f(152 , 408)
    glVertex2f(177 , 407)
    glVertex2f(178 , 406)
    glVertex2f(179 , 405)
    glVertex2f(180 , 404)
    glVertex2f(181 , 402)
    glVertex2f(185 , 396)
    glVertex2f(185 , 394)
    glVertex2f(186 , 393)
    glVertex2f(186 , 392)
    glVertex2f(184 , 392)
    glVertex2f(182 , 391)
    glVertex2f(180 , 391)
    glVertex2f(172 , 390)
    glVertex2f(153 , 390)
    glVertex2f(152 , 390)
    glVertex2f(152 , 390)
    glEnd()
    # ornamen
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINES)
    glVertex2f(52 , 371)
    glVertex2f(70 , 371)
    glEnd()
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINES)
    glVertex2f(60 , 377)
    glVertex2f(65 , 377)
    glVertex2f(67 , 376)
    glVertex2f(69 , 375)
    glVertex2f(80 , 374)
    glEnd()
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(55 , 377)
    glVertex2f(56 , 376)
    glVertex2f(58 , 376)
    glVertex2f(59 , 376)
    glVertex2f(60 , 377)
    glVertex2f(60 , 380)
    glEnd()
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(55 , 377)
    glVertex2f(57 , 382)
    glVertex2f(58 , 383)
    glVertex2f(60 , 380)
    glEnd()
    glColor3ub(255 , 255 ,255)
    glBegin(GL_POLYGON)
    glVertex2f(190 , 378)
    glVertex2f(191 , 380)
    glVertex2f(191 , 382)
    glVertex2f(192 , 384)
    glVertex2f(193 , 385)
    glVertex2f(194 , 387)
    glVertex2f(195 , 387)
    glVertex2f(196 , 386)
    glVertex2f(198 , 385)
    glVertex2f(199 , 384)
    glVertex2f(199 , 383)
    glVertex2f(200 , 380)
    glVertex2f(200 , 378)
    glEnd()
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINES)
    glVertex2f(192 , 378)
    glVertex2f(193 , 380)
    glVertex2f(194 , 382)
    glVertex2f(194 , 383)
    glVertex2f(195 , 384)
    glVertex2f(196 , 383)
    glVertex2f(197 , 382)
    glVertex2f(198 , 382)
    glVertex2f(200 , 380)
    glEnd()
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINES)
    glVertex2f(182 , 372)
    glVertex2f(202 , 372)
    glEnd()
    glColor3ub(0 , 0 , 0)
    glBegin(GL_LINES)
    glVertex2f(183 , 375)
    glVertex2f(185 , 376)
    glVertex2f(186 , 377)
    glVertex2f(188 , 378)
    glVertex2f(189 , 378)
    glVertex2f(202 , 378)
    glEnd()

def PointSoal():
    #POINTSOAL
    glColor3ub(211, 211, 211)
    glBegin(GL_QUADS)
    glVertex2f(630, 110)
    glVertex2f(630, 140)
    glVertex2f(650, 140)
    glVertex2f(650, 110)
    glEnd()
    glColor3ub(255, 165, 0)
    glBegin(GL_QUADS)
    glVertex2f(610, 140)
    glVertex2f(670, 140)
    glVertex2f(670, 180)
    glVertex2f(610, 180)
    glEnd()

def PoinFinish():
    #POINTSOAL
    glColor3ub(211, 211, 211)
    glBegin(GL_QUADS)
    glVertex2f(900, 110)
    glVertex2f(1000, 140)
    glVertex2f(1000, 140)
    glVertex2f(900, 110)
    glEnd()

def timer(value):
    global x, kecepatan, cek_point
    glutPostRedisplay()
    x -= kecepatan
    if x < value:
        x = cek_x

    # if cek_x < 20 :
    #     cek_x = 20
    glutTimerFunc(cek_point, timer, 0)
    glFlush()

def iterate():
    glViewport(0, 0, 1280, 720) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def play_player():
    kx = 20
    for i in range(10):
        Garis(kx, 70)
        kx += 235
    kx = 20
    for i in range(10):
        Garis(kx, 150)
        kx += 235

def GameMulai():
    langit()
    Jalan()
    TransKota()
    pembatas()
    kx = 20
    for i in range(10):
        Garis(kx, 70)
        kx += 235
    kx = 20
    for i in range(10):
        Garis(kx, 150)
        kx += 235
    Awan()
    PointSoal()
    mobil()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    GameMulai()
    glFlush()
    glutSwapBuffers()

def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Test")
    glutDisplayFunc(showScreen)
    # glutMouseFunc(iniHandleMouse)
    # glutPassiveMotionFunc(mouseFunc)
    # glutTimerFunc(20, timer, 10)
    timer(20)
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()