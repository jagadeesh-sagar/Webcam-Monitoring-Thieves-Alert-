import cv2
import time

video=cv2.VideoCapture(0)
time.sleep(2)

while True:
    check, frame=video.read()
    cv2.imshow("my_video",frame)

    key = cv2.waitKey(1)


    if key == ord("q"):
        break
video.release()


