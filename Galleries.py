#test script for Gallery listing

import kairos_face
kairos_face.settings.app_id = "1efff1b3"
kairos_face.settings.app_key = "95817e68b6633112a23d0589b76a73f1"
gallery_list = kairos_face.get_galleries_names_list()
gals=gallery_list['gallery_ids']
for i in gals:
    face_list = kairos_face.get_gallery(i)
    people=face_list['subject_ids']
    print(i+' :')
    for j in people:
        print(j)