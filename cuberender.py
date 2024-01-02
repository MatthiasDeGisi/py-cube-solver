import classes.Cube as c
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def Front():
    glBegin(GL_QUADS)

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((*vertex, 1))

    glEnd()


def Back():
    glBegin(GL_QUADS)

    # # this is the same as front, but index 0 on each tuple is * -1
    # parts = [
    #     ((1, 1), (0.33, 1), (0.33, 0.33), (1, 0.33)),  # Up Left
    #     ((0.33, 1), (-0.33, 1), (-0.33, 0.33), (0.33, 0.33)),  # Up Middle
    #     ((-0.33, 1), (-1, 1), (-1, 0.33), (-0.33, 0.33)),  # Up Right
    #     ((1, 0.33), (0.33, 0.33), (0.33, -0.33), (1, -0.33)),  # Middle Left
    #     ((0.33, 0.33), (-0.33, 0.33), (-0.33, -0.33), (0.33, -0.33)),  # Middle Middle
    #     ((-0.33, 0.33), (-1, 0.33), (-1, -0.33), (-0.33, -0.33)),  # Middle Right
    #     ((1, -0.33), (0.33, -0.33), (0.33, -1), (1, -1)),  # Down Left
    #     ((0.33, -0.33), (-0.33, -0.33), (-0.33, -1), (0.33, -1)),  # Down Middle
    #     ((-0.33, -0.33), (-1, -0.33), (-1, -1), (-0.33, -1)),  # Down Right
    # ]

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((vertex[0], vertex[1] -1))

    glEnd()


def Top():
    glBegin(GL_QUADS)

    # # this is the same as front, but index 1 on each tuple is * -1
    # parts = [
    #     ((-1, -1), (-0.33, -1), (-0.33, -0.33), (-1, -0.33)),  # Up Left
    #     ((-0.33, -1), (0.33, -1), (0.33, -0.33), (-0.33, -0.33)),  # Up Middle
    #     ((0.33, -1), (1, -1), (1, -0.33), (0.33, -0.33)),  # Up Right
    #     ((-1, -0.33), (-0.33, -0.33), (-0.33, 0.33), (-1, 0.33)),  # Middle Left
    #     ((-0.33, -0.33), (0.33, -0.33), (0.33, 0.33), (-0.33, 0.33)),  # Middle Middle
    #     ((0.33, -0.33), (1, -0.33), (1, 0.33), (0.33, 0.33)),  # Middle Right
    #     ((-1, 0.33), (-0.33, 0.33), (-0.33, 1), (-1, 1)),  # Down Left
    #     ((-0.33, 0.33), (0.33, 0.33), (0.33, 1), (-0.33, 1)),  # Down Middle
    #     ((0.33, 0.33), (1, 0.33), (1, 1), (0.33, 1)),  # Down Right
    # ]

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((vertex[0], 1, -vertex[1]))

    glEnd()


def Bottom():
    glBegin(GL_QUADS)

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((vertex[0], -1, vertex[1]))

    glEnd()


def Right():
    glBegin(GL_QUADS)
    
    # # this is the same as front, but index 0 on each tuple is * -1
    # parts = [
    #     ((1, 1), (0.33, 1), (0.33, 0.33), (1, 0.33)),  # Up Left
    #     ((0.33, 1), (-0.33, 1), (-0.33, 0.33), (0.33, 0.33)),  # Up Middle
    #     ((-0.33, 1), (-1, 1), (-1, 0.33), (-0.33, 0.33)),  # Up Right
    #     ((1, 0.33), (0.33, 0.33), (0.33, -0.33), (1, -0.33)),  # Middle Left
    #     ((0.33, 0.33), (-0.33, 0.33), (-0.33, -0.33), (0.33, -0.33)),  # Middle Middle
    #     ((-0.33, 0.33), (-1, 0.33), (-1, -0.33), (-0.33, -0.33)),  # Middle Right
    #     ((1, -0.33), (0.33, -0.33), (0.33, -1), (1, -1)),  # Down Left
    #     ((0.33, -0.33), (-0.33, -0.33), (-0.33, -1), (0.33, -1)),  # Down Middle
    #     ((-0.33, -0.33), (-1, -0.33), (-1, -1), (-0.33, -1)),  # Down Right
    # ]
    
    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((1, vertex[1], -vertex[0]))
    
    glEnd()


def Left():
    glBegin(GL_QUADS)
    
    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((-1, vertex[1], vertex[0]))
    
    glEnd()

# temp list of random colours
colors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
]

parts = [
        ((-1, 1), (-0.33, 1), (-0.33, 0.33), (-1, 0.33)),  # Up Left
        ((-0.33, 1), (0.33, 1), (0.33, 0.33), (-0.33, 0.33)),  # Up Middle
        ((0.33, 1), (1, 1), (1, 0.33), (0.33, 0.33)),  # Up Right
        ((-1, 0.33), (-0.33, 0.33), (-0.33, -0.33), (-1, -0.33)),  # Middle Left
        ((-0.33, 0.33), (0.33, 0.33), (0.33, -0.33), (-0.33, -0.33)),  # Middle Middle
        ((0.33, 0.33), (1, 0.33), (1, -0.33), (0.33, -0.33)),  # Middle Right
        ((-1, -0.33), (-0.33, -0.33), (-0.33, -1), (-1, -1)),  # Down Left
        ((-0.33, -0.33), (0.33, -0.33), (0.33, -1), (-0.33, -1)),  # Down Middle
        ((0.33, -0.33), (1, -0.33), (1, -1), (0.33, -1)),  # Down Right
    ]

# proves that i can use the - so I only need one parts list
for i, part in enumerate(parts):
        for vertex in part:
            print(vertex[0])
            input("Next: ")
            print(-vertex[0])
            

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)

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
    Back()
    Top()
    Bottom()
    Right()
    Left()
    pygame.display.flip()
    pygame.time.wait(10)
