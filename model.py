from PyQt6.QtOpenGLWidgets import QOpenGLWidget 
from OpenGL.GL import *
import numpy as np


class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800,600)
        self.state = [0,0,0,0]
        self.trail1 = []
        self.trail2 = []
        self.trail3 = []
        self.max_trail_length = 10000
    def initializeGL(self):
            # glEnable(GL_BLEND)
            # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

            glClearColor(0, 0, 0, 0)  # White background
            glEnable(GL_LINE_SMOOTH)  # Anti-aliasing
        
    def resizeGL(self, w, h):
        """ Adjust viewport and projection """
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-3, 3, -2, 2, -1, 1)  # Set coordinate system
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
         
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        x = 1*np.sin(self.state[0])
        y = -1*np.cos(self.state[0])
        x2 = x+1*np.sin(self.state[2]+self.state[0])
        y2 = y-1*np.cos(self.state[2]+self.state[0])
        # x3 = x2 + 0.3*np.sin(self.state[1]+self.state[0]+self.state[2])
        # y3 = y2 - 0.3*np.cos(self.state[1]+self.state[0]+self.state[2])

        # self.trail1.append((x,y))
        self.trail2.append((x2,y2))
        # self.trail3.append((x3,y3))
        # if len(self.trail1) > self.max_trail_length:
        #     self.trail1.pop(0)
        if len(self.trail2) > self.max_trail_length:
            self.trail2.pop(0)
        # if len(self.trail3) > self.max_trail_length:
        #     self.trail3.pop(0)
            
        # glColor3f(1.0, 0.843, 0.0)  # Gold
        # glBegin(GL_LINE_STRIP)
        # for x, y in self.trail1:
        #     glVertex2f(x, y)
        # glEnd()

        glColor3f(0.0, 0.843, 0.0)  # green
        glBegin(GL_LINE_STRIP)
        for x, y in self.trail2:
            glVertex2f(x, y)
        glEnd()

        # glColor3f(0.0, 0.843, 1.0)  # Gold
        # glBegin(GL_LINE_STRIP)
        # for x, y in self.trail3:
        #     glVertex2f(x, y)
        # glEnd()


        # pendulam
        glPushMatrix()
        glRotatef(np.rad2deg(self.state[0]), 0, 0, 1)
        glBegin(GL_LINES)
        glColor4f(1.0, 0.843, 0.0, 0.2)  # gold-ish and more transparent  # fully transparent
        glVertex2f(0, 0)
        glVertex2f(0, -1)  
        glEnd()
        glPopMatrix()



        glPushMatrix()
        glRotatef(np.rad2deg(self.state[0]), 0, 0, 1)  # same as first arm
        glTranslatef(0, -1, 0)  # move to end of first pendulum
        glRotatef(np.rad2deg(self.state[2]), 0, 0, 1)  # now apply second rotation
        glBegin(GL_LINES)
        glColor4f(1.0, 0.843, 0.0, 0.2)  # gold-ish and more transparent # fully transparent
        glVertex2f(0, 0)
        glVertex2f(0, -1)  # length of second pendulum
        glEnd()
        glPopMatrix()

        # glPushMatrix()
        # glRotatef(np.rad2deg(self.state[0]), 0, 0, 1)  # same as first arm
        # glTranslatef(0, -1, 0)  # move to end of first pendulum
        # glRotatef(np.rad2deg(self.state[1]), 0, 0, 1)  # now apply second rotation
        # glTranslatef(0,-0.5,0)
        # glRotatef(np.rad2deg(self.state[2]), 0, 0, 1)
        # glBegin(GL_LINES)
        # glColor4f(1.0, 0.843, 0.0, 0.2)  # gold-ish and more transparent # fully transparent
        # glVertex2f(0, 0)
        # glVertex2f(0, -0.3)  # length of second pendulum
        # glEnd()
        # glPopMatrix()
        


