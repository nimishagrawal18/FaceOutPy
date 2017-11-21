from OperateKairos import *
import webcam
from datetime import *
import firestore
from Notification import Notify
from google.cloud import storage
import Arduino

client=storage.Client()
bucket=client.get_bucket("faceout-49a92.appspot.com")
blob=bucket.get_blob("lastface.jpg")


dbl=firestore.DBListener(2,"Listener",2)
dbl.start()
webc=webcam.Capturing(1,"Capture",1)
webc.start()
notifSent=False
while webc.isAlive():
    sec=datetime.now().second
    if sec%5==0 and webc.found:
        print("Recognization called")
        response=recognizeFile('lastface.jpg')
        if response[0]==2:
            print "Error in face Matching"
            if not notifSent and not dbl.changed:
                nowhite=Notify("New Entry!","A new person has arrived. Click to authenticate.","red")
                nowhite.sendnotif()
                firestore.upURL(firestore.genURL())
                notifSent=True


        elif response[0]==1:    #WhiteList Recognized
            print "You are " + response[1] + " confidence = {}".format(response[2])
            print 'URL=' + response[3]
            Arduino.openDoor()       #Open the door (PIN 13 of Arduino activated for 5 seconds)
            print (response[2])
            # if not notifSent:
            #     firestore.upURL(response[3])
            #     nowhite=Notify("General Alert","Whitelist person has arrived","blue")
            #     nowhite.sendnotif()
            #     notifSent=True
        elif response[0]==0:    #BlackList Recognized
            print "You are " + response[1] + " confidence = " + str(response[2])
            print 'URL=' + response[3]
            print (response[2])
            # if not notifSent:
            #     firestore.upURL(response[3])
            #     nowhite=Notify("Actual Alert","Blacklist person has arrived","red")
            #     nowhite.sendnotif()
            #     notifSent=True
    elif sec%2==0 and not webc.found:
        notifSent=False

    if dbl.changed:
        det=firestore.getDetails()  # getting list, person, timestamp, url in tuple
        if det[0]=='whitelist':
            enrollFileW("lastface.jpg",det[1])
            firestore.resetDB()

        if det[0]=='blacklist':
            enrollFileB("lastface.jpg",det[1])
            firestore.resetDB()
webc.join()
dbl.exit()
dbl.join()