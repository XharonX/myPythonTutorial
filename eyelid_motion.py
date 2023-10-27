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
        self.pupil_r = 25
        self.spacing = 0
        self.__close = False
        self.__open = True

        # open Eyes and pupils
        self.l_eye = self.draw_eye(self.left_coodinate, self.eye_width, self.eye_height, geo='circle', bg='white')
        self.r_eye = self.draw_eye(self.right_coodinate, self.eye_width, self.eye_height, geo='circle', bg='white')
        self.l_pupil = self.draw_eye(self.left_coodinate, geo='circle', bg='black', radius=25)
        self.r_pupil = self.draw_eye(self.right_coodinate, geo='circle', bg='black', radius=25)

        # For close eye
        self.l_pupil_line = self.draw_eye(self.left_coodinate, self.eye_width, geo='line', bg='black', radius=25, depth=3, state='hidden')
        self.r_pupil_line = self.draw_eye(self.right_coodinate, self.eye_width, geo='line', bg='black', radius=25, depth=3, state='hidden')

        # For emotion
        self.l_eye_arc = self.draw_eye(self.left_coodinate, self.eye_width, self.eye_height, geo='arc', bg='orange', start=180, extent=180, state='hidden', )
        self.r_eye_arc = self.draw_eye(self.right_coodinate, self.eye_width, self.eye_height, geo='arc', bg='orange', start=0, extent=180, state='hidden')

    def close(self):
        self.__close = True
        for i in range(3):
            self.canvas.scale(self.l_pupil, self.left_coodinate[0], self.left_coodinate[1], 1, 0.001)
            self.canvas.scale(self.r_pupil, self.right_coodinate[0], self.right_coodinate[1], 1, 0.001)
            print(i, f" r->{self.canvas.coords(self.r_pupil)}, l-> {self.canvas.coords(self.l_pupil)}")
            self.root.update()
            self.root.after(75)
        self.__open = False

    def open(self):
        if self.__close:
            print('eye open')

            print(f" r->{self.canvas.coords(self.r_pupil)}, l-> {self.canvas.coords(self.l_pupil)}")

            self.canvas.scale(self.l_pupil, self.left_coodinate[0], self.left_coodinate[1], 1, 2)
            # self.canvas.itemconfig(self.l_pupil, fill='black', outline='white')
            # self.canvas.itemconfig(self.r_pupil, fill='black', outline='white')
            self.root.update()
            self.root.after(100)

            self.__open = True

    def draw_eye(self, center: tuple, width=0.0, height=0.0, geo='', bg="", radius=0.0, **kwargs):
        x = center[0]
        y = center[1]
        obj = None
        try:
            # This condition is for method argument width and
            # canvas.create method args 'width' are collision
            # and confuse that is why it must be deleted.

            d = kwargs['depth']
            kwargs.__delitem__('depth')
        except KeyError:
            d = 1

        if geo == "circle":
            print(center)
            if radius > 0.0:
                obj = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=bg, outline="black", **kwargs)
            else:
                x0 = center[0] - width/2
                y0 = center[1] - height/2
                x1 = center[0] + width/2
                y1 = center[1] + height/2
                obj = self.canvas.create_oval(x0, y0, x1, y1, fill=bg, outline='black', **kwargs)
        elif geo == "line":
            print(center)
            if radius > 0:
                obj = self.canvas.create_line(x-radius, y-height, x+radius, y+height, fill=bg, width=d, **kwargs)
            else:
                obj = self.canvas.create_line(center, x+width, y+height, fill=bg, **kwargs)
        elif geo == "arc":
            obj = self.canvas.create_arc(x-width/2, y-height/2, x+width/2, y+height/2, fill=bg, width=d, **kwargs)

        return obj

    def blink(self, count=1, blink_speed=1):
        '''

        :param count:
        :param blink_speed: second
        :return: None
        '''
        pass

    def look_right(self, emotion):
        '''

        :param emotion: Currently None
        :return: None
        '''
        if self.__open:
            self.blink()
            # Write move to right
            # blink
            # first set default position
            # then move right slowly

    def look_left(self, emotion):
        '''

        :param emotion: Currently None
        :return: None
        '''
        if self.__open:
            self.blink()
            # Write move to right
            # blink
            # first set default position
            # then move right slowly

    def look_straight(self, emotion):
        '''

        :param emotion: Currently None
        :return: None
        '''
        if self.__open:
            self.blink()
            # Write move to right
            # blink
            # first set default position
            # then move right slowly

    def look_down(self, emotion):
        '''

        :param emotion: Currently None
        :return: None
        '''
        if self.__open:
            self.blink()
            # Write move to right
            # blink
            # first set default position
            # then move right slowly

    def look_up(self, emotion):
        '''

        :param emotion: Currently None
        :return: None
        '''
        if self.__open:
            self.blink()
            # Write move to right
            # blink
            # first set default position
            # then move right slowly

    def move_eye_by_mouse(self, event):
        x, y = event.x, event.y

        dx = x - self.left_coodinate[0]
        dy = y - self.left_coodinate[1]

        distance = (dx ** 2 / self.pupil_r ** 2) + (dy ** 2 / self.pupil_r ** 2)
        if distance > 1:
            angle = math.atan2(dy, dx)
            l_new_x = self.left_coodinate[0] + self.pupil_r * math.cos(angle)
            l_new_y = self.left_coodinate[1] + self.pupil_r * math.cos(angle)
        else:
            l_new_x=x
            l_new_y=y
        self.canvas.coords(self.l_pupil, l_new_x - self.pupil_r, l_new_y - self.pupil_r, l_new_x + self.pupil_r, l_new_y + self.pupil_r)

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
    FACE_HEIGHT = 600
    FACE_CENTRE_X = FACE_WIDTH / 2
    FACE_CENTRE_Y = FACE_HEIGHT / 2

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
        self.note = [i for i in range(50)]
        self.canvas.create_polygon(self.note)
        self.touch = Button(self, text="Close Eye", command=self.eyes.close)
        self.touch.pack()
        self.touch1 = Button(self, text="Open Eye", command=self.eyes.open)
        self.touch1.pack()
        self.cursor_label = Label(self, text="X: 0, Y: 0")
        self.cursor_label.pack()
        # self.canvas.bind('<Motion>', self.update_cursor_coordinates)

    def update_cursor_coordinates(self, event):
        x, y = event.x, event.y
        self.cursor_label.config(text=f"(X: {x}, Y: {y})")

    def look_fly(self):
        self.canvas.bind('<Motion>', self.eyes.move_eye_by_mouse)

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
    robot_face.look_fly()
    sleep(1)
    robot_face.mainloop()


