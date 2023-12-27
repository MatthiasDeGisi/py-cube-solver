import classes.Cube as c
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
    
def Front():
    glBegin(GL_QUADS)
    
    parts = [
        ((-1, 1), (-.33, 1), (-.33, .33), (-1, .33)),  # Up Left
        ((-.33, 1), (.33, 1), (.33, .33), (-.33, .33)),  # Up Middle
        ((.33, 1), (1, 1), (1, .33), (.33, .33)),  # Up Right
        ((-1, .33), (-.33, .33), (-.33, -.33), (-1, -.33)),  # Middle Left
        ((-.33, .33), (.33, .33), (.33, -.33), (-.33, -.33)),  # Middle Middle
        ((.33, .33), (1, .33), (1, -.33), (.33, -.33)),  # Middle Right
        ((-1, -.33), (-.33, -.33), (-.33, -1), (-1, -1)),  # Down Left
        ((-.33, -.33), (.33, -.33), (.33, -1), (-.33, -1)),  # Down Middle
        ((.33, -.33), (1, -.33), (1, -1), (.33, -1)),  # Down Right
    ]

    colors = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),  # Replace with your specific colors
        (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 1, 1), (1, 0, 0), (0, 1, 0),
    ]

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((*vertex, 1))

    glEnd()

def Back():
    glBegin(GL_QUADS)
    
    parts = [
        ((-1, 1), (-.33, 1), (-.33, .33), (-1, .33)),  # Up Left
        ((-.33, 1), (.33, 1), (.33, .33), (-.33, .33)),  # Up Middle
        ((.33, 1), (1, 1), (1, .33), (.33, .33)),  # Up Right
        ((-1, .33), (-.33, .33), (-.33, -.33), (-1, -.33)),  # Middle Left
        ((-.33, .33), (.33, .33), (.33, -.33), (-.33, -.33)),  # Middle Middle
        ((.33, .33), (1, .33), (1, -.33), (.33, -.33)),  # Middle Right
        ((-1, -.33), (-.33, -.33), (-.33, -1), (-1, -1)),  # Down Left
        ((-.33, -.33), (.33, -.33), (.33, -1), (-.33, -1)),  # Down Middle
        ((.33, -.33), (1, -.33), (1, -1), (.33, -1)),  # Down Right
    ]

    colors = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),  # Replace with your specific colors
        (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 1, 1), (1, 0, 0), (0, 1, 0),
    ]

    for i, part in enumerate(parts):
        glColor3fv(colors[i])
        for vertex in part:
            glVertex3fv((*vertex, -1))

    glEnd()

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
    pygame.display.flip()
    pygame.time.wait(10)
