import cv2
import awslib

cap = cv2.VideoCapture(1)


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


if __name__ == "__main__":
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # imen = cv2.imencode('.jpg', frame)[1].tostring()
        # awslib.detect(imen)

        rects = detect(gray, cascade)

        if len(rects) != 0:
            try:
                imen = cv2.imencode('.jpg', frame)[1].tostring()
                awslib.detect(imen)
            except Exception as e:
                raise e

        cv2.imshow('test', frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindow()
