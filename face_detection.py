import cv2


class FaceDetection:

    def __init__(self):
        self.face_count = 0
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect_faces(self, image):
        faces = self.face_cascade.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(10, 10)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        return faces
