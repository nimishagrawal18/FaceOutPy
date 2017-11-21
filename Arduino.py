import serial
import time

def openDoor():
    try:
        ser=serial.Serial('COM3',9600)
        tym=time.time()
        while 1:
            ser.write('H')
            if time.time()==(tym+5):  # Keep signal on for 5 sec
                ser.write('L')
                break
    except serial.serialutil.SerialException:
        print("Serial Port Error!")
