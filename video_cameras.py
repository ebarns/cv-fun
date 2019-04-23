import cv2


class VideoCameras:

    def __init__(self, num_of_cameras):
        self.video_captures = [self.create_video_capture_device(i - 1) for i in range(1, num_of_cameras + 1)]

    @staticmethod
    def create_video_capture_device(device_count):
        print(device_count)
        video_capture = cv2.VideoCapture(device_count)
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
        return video_capture

    def get_frames(self):
        return [self.get_grayscale_frame(video_capture) for video_capture in self.video_captures]

    @staticmethod
    def get_grayscale_frame(video_capture):
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    @staticmethod
    def display_frames(frames):
        for i in range(len(frames)):
            cv2.imshow(f'CAPTURE_{i}', frames[i])

    def release(self):
        for video_capture in self.video_captures:
            video_capture.release()
