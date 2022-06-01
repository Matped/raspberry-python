import os
import firebase_admin
from firebase_admin import db

# to get the location of the json file.
baseDir = os.path.dirname(os.path.abspath(__file__))

# join path with the filename
certFile = os.path.join(baseDir, 'apptracker-cadd4-firebase-adminsdk-i2agg-9ddab7a2a9.json')

# credential object for database and initialization of firebase.
credObj = firebase_admin.credentials.Certificate(certFile)
defaultApp = firebase_admin.initialize_app(credObj, {
    'databaseURL': 'https://apptracker-cadd4-default-rtdb.europe-west1.firebasedatabase.app/'})

# firebase database methods.
ref = db.reference("/Items/TheBar/")
