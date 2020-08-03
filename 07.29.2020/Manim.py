from manimlib.imports import *

class ThreeDSurface(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 12,
        "v_min": 0,
        "v_max": 25,
        "resolution": 13,
        "surface_piece_config": {},
        "fill_color": BLUE_D,
        "fill_opacity": 0.0,
        "stroke_color": LIGHT_GREY,
        "stroke_width": 0.5,
        "should_make_jagged": False,
        "pre_function_handle_to_anchor_scale_factor": 0.00001,
        "checkerboard_colors": [BLUE_D]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        f = []
        my_name_is_array = []
        with open("array_for_my_name_is_array.txt") as f:
            for line in f:
                my_name_is_array.append([int(i) for i in line.split()])
        
        #print(my_name_is_array)
        return np.array([x,y,my_name_is_array[int(x)][int(y)]])


class Test(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(0.6, -0.7853981, distance=10)
        self.move_camera(0.7*np.pi/2, 0.40*np.pi)

        surface = ThreeDSurface()
        self.play(ShowCreation(surface))

        #d = Dot(np.array([0,0,0]), color = YELLOW)
        #self.play(ShowCreation(d))

        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(9)