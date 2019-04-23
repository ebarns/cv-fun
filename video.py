import cv2

from face_detection import FaceDetection
from frame_morph import FaceFrameMorpher
from video_cameras import VideoCameras
from video_recorder import VideoRecorder


class Spoopy:

    def __init__(self, num_of_cameras=1, record_video=False):
        self.is_capturing_video = True
        self.video_cameras = VideoCameras(num_of_cameras)
        self.record_video = record_video
        self.face_detection = FaceDetection()
        self.face_frame_morpher = FaceFrameMorpher()
        self.video_recorder = VideoRecorder()

    def capture_video(self):
        while self.is_capturing_video:
            frames = self.video_cameras.get_frames()

            frames = self.face_frame_morpher.morph_frame_faces(frames)

            self.video_cameras.display_frames(frames)
            self.kill_capture()

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


cam = Spoopy()
cam.capture_video()
