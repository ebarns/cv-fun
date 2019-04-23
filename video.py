import cv2
import numpy as np

from frame_morph import FrameMorph
from face_detection import FaceDetection
from video_cameras import VideoCameras
from video_recorder import VideoRecorder


class Spoopy:

    def __init__(self, num_of_cameras=1, record_video=False):
        self.is_capturing_video = True
        self.video_cameras = VideoCameras(num_of_cameras)
        self.record_video = record_video
        self.face_detection = FaceDetection()
        self.frame_morpher = FrameMorph()
        self.video_recorder = VideoRecorder()

    def capture_video(self):
        while self.is_capturing_video:
            frames = self.video_cameras.get_frames()

            self.morph_frame_faces(frames)

            self.video_cameras.display_frames(frames)
            self.kill_capture()

    def morph_frame_faces(self, frames):
        for frame in frames:
            faces = self.face_detection.detect_faces(frame)
            if len(faces) == 0:
                self.frame_morpher.reset_animation()
            for (x, y, w, h) in faces:
                self.frame_morpher.morph_pixels_in_area_animated(frame, x, y, w, h)

    def write_video(self, frame):
        if self.record_video:
            self.video_recorder.write_video_frame(frame)

    def kill_capture(self):
        if cv2.waitKey(33) == ord('a'):
            print("Tearing down capture")
            self.is_capturing_video = False
            self.video_cameras.release()
            self.video_recorder.stop_video_record()
            cv2.destroyAllWindows()

    @staticmethod
    def merge_images(img1, img2, img3):
        return np.hstack(np.hstack((img1, img2)), img3)


cam = Spoopy(False)
cam.capture_video()
