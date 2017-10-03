# Main script for function usage

import kairos_face
# from webcam import *


def enrollFileW(path, person_name):
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    kairos_face.enroll_face(file=path, subject_id=person_name, gallery_name='whitelist')
    print('Enrolled in whitelist: ' + person_name)


def enrollW(img, person_name):
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    kairos_face.enroll_face(base64_image_contents=img, subject_id=person_name, gallery_name='whitelist')  #Not sure about how to pass the object
    print('Enrolled in blacklist: ' + person_name)


def enrollFileB(path, person_name):
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    kairos_face.enroll_face(file=path, subject_id=person_name, gallery_name='blacklist')
    print('Enrolled in blacklist: ' + person_name)


def enrollB(img, person_name):
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    kairos_face.enroll_face(file=img, subject_id=person_name, gallery_name='blacklist')
    print('Enrolled in blacklist: ' + person_name)


def recognizeFile(path):
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    try:
        recog = kairos_face.recognize_face(file=path, gallery_name="whitelist")
        found = recog['images'][0]['transaction']['status']
        if found == 'success':
            print ('Face found in Whitelist')
            person = recog['images'][0]['transaction']['subject_id']
            confidence = recog['images'][0]['transaction']['confidence']
            print (found)
            print("The person is " + person + " with %d percent confidence in whitelist." % (confidence * 100))
            return 1,person,confidence
        else:
            recog = kairos_face.recognize_face(file=path,gallery_name="blacklist")
            found = recog['images'][0]['transaction']['status']
            if found == 'success':
                print ('Face found in Blacklist')
                person = recog['images'][0]['transaction']['subject_id']
                confidence = recog['images'][0]['transaction']['confidence']
                print (found)
                print("The person is " + person + " with %d percent confidence in blacklist." % (confidence * 100))
                return 0, person, confidence
    except kairos_face.exceptions.ServiceRequestError:
        print('gallery not found')
    except:
        print ('ERROR!!')


def galleryPrint(): # tolist all galleries along with subject
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    gallery_list = kairos_face.get_galleries_names_list()
    gals = gallery_list['gallery_ids']
    for i in gals:
        face_list = kairos_face.get_gallery(i)
        people = face_list['subject_ids']
        print(i + ' :')
        for j in people:
            print(j)
# galleryPrint()

def getGallery():  # to get the list of all galleries
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    gallery_list = kairos_face.get_galleries_names_list()
    gals = gallery_list['gallery_ids']
    for i in gals:
        face_list = kairos_face.get_gallery(i)
        people = face_list['subject_ids']
        yield i


def getPeople(gal):  # pass the gallery name here
    kairos_face.settings.app_id = "1efff1b3"
    kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
    face_list = kairos_face.get_gallery(gal)
    people = face_list['subject_ids']
    for j in people:
        yield j

for i in getGallery():
    print i
