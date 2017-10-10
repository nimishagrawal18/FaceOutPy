# test script for Recognition
import Arduino
import kairos_face
kairos_face.settings.app_id = "1efff1b3"
kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
try :
    recog=kairos_face.recognize_face(file="lastface.jpg",gallery_name="whitelist")
    print('Found in gallery')
    try:
        found = recog['images'][0]['transaction']['status']
        person = recog['images'][0]['transaction']['subject_id']
        confidence = recog['images'][0]['transaction']['confidence']
        print (found)
        print("The person is "+person+" with %d percent confidence." %(confidence*100))
        if confidence>=0.65:
            try:
                Arduino.led()
            except Arduino.SerialError:
                print "Unable to open door!"
    except ValueError:
        err=recog['Errors']
        print("the following errors were recieved -")
        for i in err:
            print i
except kairos_face.exceptions.ServiceRequestError :
    print('gallery not found')
#except :
 #   print ('ERROR!!')