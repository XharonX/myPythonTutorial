from tkinter import *
from customtkinter import *

from math import pi, sin, cos, radians
from eyes import Eyes


class Face(Tk):
    FACE_WIDTH = 1000
    FACE_HEIGHT = 600
    FACE_CENTRE_X = FACE_WIDTH / 2
    FACE_CENTRE_Y = FACE_HEIGHT / 2

    def __init__(self):
        super().__init__()
        self.title("Eye motion Project")
        self.mainFrame = Frame(self, width=Face.FACE_WIDTH, height=Face.FACE_HEIGHT, bg='black')
        self.mainFrame.pack()
        self.eyeFrame = Frame(self.mainFrame, width=Face.FACE_WIDTH, height=int(Face.FACE_HEIGHT/3))
        self.eyeFrame.pack()
        self.canvas = Canvas(self.eyeFrame, width=self.FACE_WIDTH, height=self.FACE_HEIGHT,  bg='#ffae42')
        self.canvas.pack()
        self.eyes = Eyes(self, self.canvas)

    def anger_face(self):
        pass

    def happy_face(self):
        pass

    def smile(self):
        pass

    def laugh(self):
        pass

    def sad(self):
        pass



