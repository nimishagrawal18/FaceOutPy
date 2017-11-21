# main video capture script
import cv2
import logging as log
import datetime as dt
from time import sleep
import threading


class Capturing(threading.Thread):
    found=False

    def __init__(self,threadid,name,counter):
        threading.Thread.__init__(self)
        self.threadid=threadid
        self.name=name
        self.counter=counter


    def run(self):
        print("Starting Capturing Thread")
        cascPath = "C:\Users\\nimis\PycharmProjects\FaceOutPy\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        log.basicConfig(filename='webcam.log', level=log.INFO)

        video_capture = cv2.VideoCapture(0)
        anterior = 0

        while True:
            if not video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass

            # Capture frame-by-frame
            ret, frame = video_capture.read()
            face = frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            Capturing.found=False
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            if len(faces) >= 1:
                # count = count + 1
                # cv2.imwrite("Capture\\face %d.jpg" % count, frame)
                cv2.imwrite("lastface.jpg", face)
                Capturing.found=True

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if anterior != len(faces):
                anterior = len(faces)
                log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

