import classes.Cube as c

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    # # From me 8v
    # (-.33, 1, 1),
    # (0.33, 1, 1),
    # (-.33, -1, 1),
    # (0.33, -1, 1),
    # #12v
    # (-1, -.33, 1),
    # (-1, 0.33, 1),
    # (1, -.33, 1),
    # (1, 0.33, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
    # # from me
    # (8, 10),
    # (9, 11),
    # (12, 14),
    # (13, 15),
)

colors = (
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Cyan
    (1, 1, 1),  # White
)


# def Cube():
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             print(verticies[vertex])
#             glVertex3fv(verticies[vertex])
#     glEnd()

# def FrontTest():
#     glBegin(GL_QUADS)
#     glColor3fv(colors[0])
#     glVertex3fv((-1, -1, 0))
#     glVertex3fv((-1, 0, 0))
#     glVertex3fv((0, 0, 0))
#     glVertex3fv((0, -1, 0))
#     glColor3fv(colors[1])
#     glVertex3fv((0, -1, 0))
#     glVertex3fv((1, -1, 0))
#     glVertex3fv((1, 0, 0))
#     glVertex3fv((0, 0, 0))
#     glEnd()
    
def Front():
    glBegin(GL_QUADS)
    # Up Left
    glColor3fv(colors[0])
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-.33, 1, 1))
    glVertex3fv((-.33, .33, 1))
    glVertex3fv((-1, .33, 1))
    # Up Middle
    glColor3fv(colors[1])
    glVertex3fv((-.33, 1, 1))
    glVertex3fv((.33, 1, 1))
    glVertex3fv((.33, .33, 1))
    glVertex3fv((-.33, .33, 1))
    # Up Right
    glColor3fv(colors[2])
    glVertex3fv((.33, 1, 1))
    glVertex3fv((1, 1, 1))
    glVertex3fv((1, .33, 1))
    glVertex3fv((.33, .33, 1))
    # Middle Left
    glColor3fv(colors[3])
    glVertex3fv((-1, .33, 1))
    glVertex3fv((-.33, .33, 1))
    glVertex3fv((-.33, -.33, 1))
    glVertex3fv((-1, -.33, 1))
    # Middle Middle
    glColor3fv(colors[4])
    glVertex3fv((-.33, .33, 1))
    glVertex3fv((.33, .33, 1))
    glVertex3fv((.33, -.33, 1))
    glVertex3fv((-.33, -.33, 1))
    # Middle Right
    glColor3fv(colors[5])
    glVertex3fv((.33, .33, 1))
    glVertex3fv((1, .33, 1))
    glVertex3fv((1, -.33, 1))
    glVertex3fv((.33, -.33, 1))
    # Down Left
    glColor3fv(colors[6])
    glVertex3fv((-1, -.33, 1))
    glVertex3fv((-.33, -.33, 1))
    glVertex3fv((-.33, -1, 1))
    glVertex3fv((-1, -1, 1))
    # Down Middle
    glColor3fv(colors[0])
    glVertex3fv((-.33, -.33, 1))
    glVertex3fv((.33, -.33, 1))
    glVertex3fv((.33, -1, 1))
    glVertex3fv((-.33, -1, 1))
    # Down Right
    glColor3fv(colors[1])
    glVertex3fv((.33, -.33, 1))
    glVertex3fv((1, -.33, 1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((.33, -1, 1))
    glEnd()
    

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Front()
    pygame.display.flip()
    pygame.time.wait(10)
