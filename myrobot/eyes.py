from math import sin, cos, pi, radians


class Eyes:
    def __init__(self, root, canvas):
        self.root = root
        self.c = canvas
        self.left_origin = (self.root.FACE_WIDTH / 4, self.root.FACE_HEIGHT / 3)
        self.right_origin = (self.root.FACE_WIDTH * 3/4, self.root.FACE_HEIGHT / 3)

        self.eye_x_radius = 200
        self.eye_y_radius = 150
        self.pupil_radius = 25
        self.__close = False
        self.__open = True

        # create left and right eyes
        self.l_eye = self.draw_eye(self.left_origin[0], self.left_origin[1], self.eye_x_radius, self.eye_y_radius, 50, )
        self.r_eye = self.draw_eye(self.right_origin[0], self.right_origin[1], self.eye_x_radius, self.eye_y_radius, -10)

    def draw_eye(self, x_center, y_center, radius_x, radius_y, rotate_angle=10):
        rad = radians(rotate_angle)
        points = 360
        # 360 deg -> 2π
        # each deg has 0.0174533 radian if divided by 360

        radian = 2 * pi / points
        step_points = []
        for i in range(points):
            # cos refer to x axis cos x = A/H
            x = x_center + radius_x * cos(i * radian)
            # sin refer to y axis sin x = O/H
            y = y_center + radius_y * sin(i * radian)
            dx = x - x_center
            dy = y - y_center
            print(dx, dy)
            x_rotated = dx * cos(rad) - dy * sin(rad) + x_center
            y_rotated = dx * sin(rad) - dy * cos(rad) + y_center
            step_points.append((x_rotated, y_rotated))
            # step_points.append((x, y))

            # if rotate_angle == 0:
            #     step_points.append((x, y))
            # else:
            #     print(step_points)

        eye = self.c.create_polygon(step_points, fill='blue', outline='blue', width=2, )
        return eye
