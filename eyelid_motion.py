from tkinter import *
from time import sleep


class Eyes:
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.eye_width = 240
        self.eye_height = 300
        self.blinking_factor = 1
        self.pupil_width = 50
        self.spacing = 350
        self.x_centre_p = (200 - 150)/2
        self.y_centre_p = (100 - 200)/2
        self.l_eye = self.canvas.create_oval(150, 100, (1000/4), 200)   # need to calculate
        self.r_eye = self.canvas.create_oval(1000*3/4, 100, (1000*3/4)+100, 200)
        self.l_pupil = self.canvas.create_oval(self.x_centre_p - 50, self.y_centre_p - 50 , self.x_centre_p+50, self.y_centre_p + 50, fill='black')
        # self.r_pupil = self.canvas.create_oval(100,50, 150, 100)

    def close(self):
        x1, y1, x2, y2 = self.canvas.coords(self.r_eye)
        centre_x = (x1 + x2) / 2
        centre_y = (y1 + y2) / 2
        self.canvas.scale(self.r_eye, centre_x, centre_y, 1, 0.002)

    def open(self):
        x1, y1, x2, y2 = self.canvas.coords(self.r_eye)
        centre_x = (x1+ x2) / 2
        centre_y = (y1+ y2) / 2

        self.canvas.scale(self.r_eye, centre_x, centre_y, 1, 1/0.002)
    def draw_eye(self):
        pass


class Face(Tk):
    FACE_WIDTH = 1000
    FACE_HEIGHT = 500

    def __init__(self):
        super().__init__()
        self.title("Face motion Project")
        self.canvas = Canvas(self, width=Face.FACE_WIDTH, height=Face.FACE_HEIGHT, background='#ffae42',)
        self.canvas.pack()
        self.eyes = Eyes(self.canvas)
        self.nose = None
        self.mouse = None


robot_face = Face()
# robot_face.eyes.open()
sleep(1)
# robot_face.eyes.close()
robot_face.mainloop()


