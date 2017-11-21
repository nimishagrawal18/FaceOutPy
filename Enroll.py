# test script for face enrollment

import kairos_face
#from webcam import *
kairos_face.settings.app_id = "1efff1b3"
kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
kairos_face.enroll_face(file='lastface.jpg',subject_id='Sir',gallery_name='whitelist')
