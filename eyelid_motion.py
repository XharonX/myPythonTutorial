from tkinter import *
from time import sleep
import math


class Eyes:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.left_coodinate = (Face.FACE_WIDTH/4, Face.FACE_HEIGHT/3)
        self.right_coodinate = (Face.FACE_WIDTH * 3/4, Face.FACE_HEIGHT/3)
        self.eye_ball_color = '#eee'
        self.center_point = None
        self.skin_color = None
        self.eye_width = 150
        self.eye_height = 150
        self.pupil_width = 50

        self.__close = False
        self.__open = True

        self.l_eye = self.draw_eye(self.left_coodinate, self.eye_width, self.eye_height, 'white')
        self.r_eye = self.draw_eye(self.right_coodinate, self.eye_width, self.eye_height, 'white')
        self.l_pupil = self.draw_eye(self.left_coodinate, self.pupil_width, self.pupil_width, 'black')
        self.r_pupil = self.draw_eye(self.right_coodinate, self.pupil_width, self.pupil_width, 'black')

    def close(self):
        self.__close = True
        for i in range(10):
            self.canvas.scale(self.l_pupil, self.left_coodinate[0], self.left_coodinate[1], 1.1, 0.77)
            self.canvas.scale(self.r_pupil, self.right_coodinate[0], self.right_coodinate[1], 1.1, 0.77)
            self.canvas.move(self.l_pupil, 0, 4)
            self.canvas.move(self.r_pupil, 0, 4)
            self.root.update()
            self.root.after(75)
            self.__open = False

    def open(self):
        if self.__close:
            print('eye open')
            for i in range(9):
                self.canvas.scale(self.l_pupil, self.left_coodinate[0], self.left_coodinate[1], 0.9, 1.33)
                self.canvas.scale(self.r_pupil, self.right_coodinate[0], self.right_coodinate[1], 0.9, 1.33)
                self.canvas.move(self.r_pupil, 0, -5.8)
                self.root.update()
            self.root.update()
            self.root.after(100)
            self.__open = True

    def draw_eye(self, center: tuple, width, height, bg, **kwargs):
        x0 = center[0] - width/2
        y0 = center[1] - height/2
        x1 = center[0] + width/2
        y1 = center[1] + height/2
        obj = self.canvas.create_oval(x0, y0, x1, y1, fill=bg, outline='black', **kwargs)
        return obj


class Nose:
    def __init__(self, canvas):
        self.canvas = canvas


class Mouth:
    def __init__(self, canvas):
        self.canvas = canvas


    def drawing(self):
        pass

    def laugh(self):
        pass

    def smile(self):
        pass

    def angry(self):
        pass

    def hungry(self):
        pass


class Face(Tk):
    FACE_WIDTH = 1000
    FACE_HEIGHT = 500
    FACE_CENTRE = FACE_WIDTH / 2

    def __init__(self):
        super().__init__()
        self.title("Face motion Project")
        self.eyeFrame = Frame(self, width=1000, height=300, background='black')
        self.eyeFrame.pack()
        self.canvas = Canvas(self.eyeFrame, width=Face.FACE_WIDTH, height=Face.FACE_HEIGHT, background='#ffae42')
        self.canvas.pack()
        self.eyes = Eyes(self, self.canvas)
        self.nose = Nose(self.canvas)
        self.mouse = Mouth(self.canvas)
        self.touch = Button(self, text="Close Eye", command=self.eyes.close)
        self.touch.pack()
        self.touch1 = Button(self, text="Open Eye", command=self.eyes.open)
        self.touch1.pack()

    def anger_face(self):
        pass

    def happy_face(self):
        pass

    def smile(self):
        pass

    def laugh(self):
        pass

    def touch_from_left(self):
        pass
    def touch_from_right(self):
        pass


if __name__ == '__main__':
    robot_face = Face()
    sleep(1)
    robot_face.mainloop()


