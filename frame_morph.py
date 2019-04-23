import math

import numpy as np

from face_detection import FaceDetection


class FaceFrameMorpher:

    def __init__(self):
        self.animated_scale = 0.0
        self.animated_direction = 1
        self.face_detection = FaceDetection()
        self.MAX_ANIMATION_SCALE = 50.0

    def morph_frame_faces(self, frames):
        for frame in frames:
            faces = self.face_detection.detect_faces(frame)
            if len(faces) == 0:
                self.reset_animation()
            for (x, y, w, h) in faces:
                self.morph_pixels_in_area_animated(frame, x, y, w, h)

        return frames

    def animated_scale_tick(self):
        self.animated_scale += self.animated_direction
        if self.animated_scale == -self.MAX_ANIMATION_SCALE or self.animated_scale == self.MAX_ANIMATION_SCALE:
            self.animated_direction = -1 * self.animated_direction

    def reset_animation(self):
        self.animated_scale = 0.0

    def morph_pixels_in_area_animated(self, img, x_pos, y_pos, width, height):
        section = img[y_pos: y_pos + height, x_pos:x_pos + width]
        self.animated_scale_tick()
        section = FaceFrameMorpher.vertical_wave(section, self.animated_scale)
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
