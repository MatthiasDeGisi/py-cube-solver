    """Might have to scrap this one :(
    """

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

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((vertex[0], vertex[1], -1))

    glEnd()


def Top():
    glBegin(GL_QUADS)

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


def Render_Cube():
    """Renders the cube sides, updates the screen and waits 10ms"""
    Front()
    Back()
    Top()
    Bottom()
    Right()
    Left()
    pygame.display.flip()
    pygame.time.wait(10)


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

# # broken currently
# x_rotation_vectors = [(1, 0, 0), (0, 0, -1), (-1, 0, 0), (0, 0, 1)]

x_rotation_counter = 0

# y_rotation_vectors = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]

y_rotation_counter = 0

# init pygame and openGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)

# set up the camera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

# move the camera back
glTranslatef(0.0, 0.0, -5)

# tiny rotate to give some perspective
glRotatef(-23, -1, 1, 0)

# saves the current matrix state
glPushMatrix()

while True:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # renders all sides of the cube
    Render_Cube()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # rotates the cube front side to top (x-axis)
        if event.type == KEYDOWN and event.key == K_x:
            
            for i in range(6):
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glRotatef(-15, 1, 0, 0)
                Render_Cube()

            # changes the rotation counter, which in turn references a
            # different rotation vector when rotating y-axis
            y_rotation_counter += 1 if y_rotation_counter < 3 else -3
            
        # rotates the cube front side to left (y-axis)
        if event.type == KEYDOWN and event.key == K_y:

            for i in range(6):
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glRotatef(-15, 0, 1, 0)
                # glRotatef(-15, *y_rotation_vectors[y_rotation_counter])
                Render_Cube()

            # changes the rotation counter, which in turn references a
            # different rotation vector when rotating x-axis
            x_rotation_counter += 1 if x_rotation_counter < 3 else -3

