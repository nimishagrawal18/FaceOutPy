from google.cloud import firestore
import datetime
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading
from google.cloud import storage

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\nimis\\PycharmProjects\\FaceOutPy\\faceout-49a92-firebase-adminsdk.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceout-49a92.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules

client=storage.Client()
bucket=client.get_bucket("faceout-49a92.appspot.com")
blob=bucket.get_blob("lastface.jpg")


fsdb=firestore.Client()   # Original code
   # Original code
def upWhitelist(name,confidence,pic):
    pass
    whitelist=fsdb.collection('whitelist')
    whitelist.document().set({'personName':name,'confidence':confidence,'picURL':pic})

def upBlacklist(name,confidence,pic):
    pass
    whitelist=fsdb.collection('blacklist')
    whitelist.document().set({'personName':name,'confidence':confidence,'picURL':pic})

def upURL(imgURL):
    ref = db.reference('url')
    ts=datetime.datetime.now()
    ts=time.mktime(ts.timetuple())
    ref.set(imgURL)
    tsref = db.reference('timestamp')
    tsref.set(ts)
    print 'URL uploaded with timestamp'

def genURL():
    blob.upload_from_filename("lastface.jpg")
    ts = datetime.datetime.now()
    ts = int(time.mktime(ts.timetuple())+259200 )    #72 hours
    url = blob.generate_signed_url(ts)
    return url




def getDetails():
    return (db.reference('list').get(),db.reference('person').get(),db.reference('timestamp').get(),db.reference('url').get())

def resetDB():
    db.reference('list').set("")
    db.reference('person').set("")

class DBListener(threading.Thread):
    changed=False
    toexit=False
    def __init__(self,threadid,name,counter):
        threading.Thread.__init__(self)
        self.threadid=threadid
        self.name=name
        self.counter=counter

    def exit(self):
        DBListener.toexit=True

    def run(self):
        print("Starting Listener Thread")
        DBListener.changed=True

        while not DBListener.toexit:
            li=db.reference('list').get()
            nam=db.reference('person').get()
            if nam=="" or li=="":
                DBListener.changed=False
            else:
                DBListener.changed=True


