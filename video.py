import cv2
import numpy as np

from frame_morph import FrameMorph
from face_detection import FaceDetection


class VideoCamera:

    def __init__(self, record_video=False, num_of_cameras=1):
        self.current_frame = None
        self.is_capturing_video = True
        self.video_captures = [self.create_video_capture_device(i - 1) for i in range(1, num_of_cameras + 1)]
        self.record_video = record_video
        self.face_detection = FaceDetection()
        self.frame_morpher = FrameMorph()
        if record_video:
            self.video_output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    @staticmethod
    def create_video_capture_device(device_count):
        print(device_count)
        video_capture = cv2.VideoCapture(device_count)
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
        return video_capture

    def capture_video(self):
        while self.is_capturing_video:
            frames = VideoCamera.get_frames(self.video_captures)

            self.morph_frame_faces(frames)

            VideoCamera.display_frames(frames)
            self.kill_capture()

    @staticmethod
    def get_frames(video_captures):
        return [VideoCamera.get_frame(video_capture) for video_capture in video_captures]

    @staticmethod
    def display_frames(frames):
        for i in range(len(frames)):
            cv2.imshow(f'CAPTURE_{i}', frames[i])

    @staticmethod
    def get_frame(video_capture):
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def morph_frame_faces(self, frames):
        for frame in frames:
            faces = self.face_detection.detect_faces(frame)
            for (x, y, w, h) in faces:
                self.frame_morpher.morph_pixels_in_area_animated(frame, x, y, w, h)

    def write_video(self, frame):
        if self.record_video:
            self.video_output.write(frame)

    def stop_video_record(self):
        if self.record_video:
            self.video_output.release()

    def kill_capture(self):
        if cv2.waitKey(33) == ord('a'):
            print("Tearing down capture")
            self.is_capturing_video = False
            self.video_capture.release()
            self.stop_video_record()
            cv2.destroyAllWindows()

    @staticmethod
    def merge_images(img1, img2, img3):
        return np.hstack(np.hstack((img1, img2)), img3)


cam = VideoCamera(False)
cam.capture_video()
