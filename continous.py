from OperateKairos import *
import webcam
import threading

webcam.capture()
bw,prsn,conf=recognizeFile('lastface.jpg')
