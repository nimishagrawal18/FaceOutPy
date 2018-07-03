# FaceOutPy
![FaceOut logo](https://github.com/nimishagrawal18/FaceOutPy/blob/master/FaceOut%20Logo%2001.png "Logo")

Python (core) module for faceOut

This Software Aims to provide safety to the house of the user of the system.

*In recent years, human detection techniques, especially those implemented by face detection strategies, have been successfully applied to many consumer products such as digital cameras, smart phones, or surveillance systems for detecting people. Adding to these ideas, in era of IoT,when everything is being connected to internet it is vital to implement this technology to enhance the security of doors as well which can be controlled remotely through smartphones and computer.*

Controlling door lock through Face Recognition System will be facilitated with control over Android mobile phone. Because of the usability of the face recognition, this idea and its algorithms can be used in many other areas like defence, aiding differently abled people etc.

The project is divided into two main modules-
1. Central Control module based on Python 2.7.x
2. Android app Used for user interaction.

## Control Module
This module provides the core functionality to the System. This module currently utilises the *Kairos* cloud based Face Recognition API (we plan on utilising a local module for this soon) to recognise and classify the faces captured from the Camera that is installed at the door.
If the detected face matches with the existing database and the person is recognised with a considerable confidence, the door is automatically unlocked if the person in question is enrolled in the "Whitelist".
If the person is unknown or is enrolled in the "Blacklist", a notification is sent to the Android based module, confirming the actions to be taken along with the identity (*if available*) and a Snapshot from the camera.
The locking/unlocking of the door is controlled using an **Arduino Uno** connected to the system via a Serial interface.

## Android App Module
**[Android App Module Repository](https://github.com/nil97/FaceOut2.0)**
This module aacts as the primary Interface with the User. It is a user friendly app which acts as a notification channel, as well as providing a UI for Enrollment of new "Contacts" as well as managing existing ones. The app supports basic functionality as of now and we plan on expanding that in the near future. When the user clicks on the recieved Notification, a UI pops up which includes the most recent snapshot of the person, along with fields for the name of the person and the choice of whether to enroll the person in the whitelist or the blacklist. Upon confirmation from the user, the set details are uploaded to Firebase and consequently enrolled in the face recognition database via the central module.

for more information contact us at <nimishagrawal.18@gmail.com>


