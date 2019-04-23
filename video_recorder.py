import cv2


class VideoRecorder:
    def __init__(self, file_name="output"):
        self.video_output = cv2.VideoWriter(f'{file_name}.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    def write_video_frame(self, frame):
        self.video_output.write(frame)

    def stop_video_record(self):
        self.video_output.release()
