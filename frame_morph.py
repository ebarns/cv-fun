import math

import numpy as np


class FrameMorph:

    def __init__(self):
        self.animated_scale = 0.0

    def animated_scale_tick(self):
        self.animated_scale += 1
        self.animated_scale %= 100.0
        # print(self.animated_scale)

    def reset_animation(self):
        self.animated_scale = 0.0

    def morph_pixels_in_area_animated(self, img, x_pos, y_pos, width, height):
        section = img[y_pos: y_pos + height, x_pos:x_pos + width]
        self.animated_scale_tick()
        section = FrameMorph.vertical_wave(section, self.animated_scale)
        print(x_pos, len(section))
        # if x_pos < len(section):
        print("morph")
        img[y_pos: y_pos + height, x_pos:x_pos + len(section)] = section

    @staticmethod
    def vertical_wave(img, wave_factor=20.0):
        img_output = np.zeros(img.shape, dtype=img.dtype)
        rows, cols = img.shape
        for i in range(rows):
            for j in range(cols):
                offset_x = int(wave_factor * math.sin(2 * 3.14 * i / 180))
                offset_y = int(wave_factor * math.sin(2 * 3.14 * j / 180))
                # print(offset_x, offset_y, i, rows)
                if j + offset_x < rows:
                    img_output[i, j] = img[abs((i + offset_y) % cols), (j + offset_x) % cols]
                else:
                    img_output[i, j] = img[i, j]

        return img_output
