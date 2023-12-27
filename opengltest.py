import classes.Cube as c
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# verticies = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1),
#     # # From me 8v
#     # (-.33, 1, 1),
#     # (0.33, 1, 1),
#     # (-.33, -1, 1),
#     # (0.33, -1, 1),
#     # #12v
#     # (-1, -.33, 1),
#     # (-1, 0.33, 1),
#     # (1, -.33, 1),
#     # (1, 0.33, 1),
# )

# edges = (
#     (0, 1),
#     (0, 3),
#     (0, 4),
#     (2, 1),
#     (2, 3),
#     (2, 7),
#     (6, 3),
#     (6, 4),
#     (6, 7),
#     (5, 1),
#     (5, 4),
#     (5, 7),
#     # # from me
#     # (8, 10),
#     # (9, 11),
#     # (12, 14),
#     # (13, 15),
# )



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
colors = (
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Cyan
    (1, 1, 1),  # White
)
    
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
