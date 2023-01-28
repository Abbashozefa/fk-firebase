from flask import Flask,render_template

from firebase_admin import db

import firebase_admin
from firebase_admin import credentials



cred_obj = firebase_admin.credentials.Certificate('flask-test-f0999-firebase-adminsdk-v2vd2-a35e9c6fce.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://flask-test-f0999-default-rtdb.firebaseio.com/'
	})
# ref = db.reference("/restaurants/")
# name = 'Vik'
# address = 'Mumbai'
# new_data = {"name": name, "address": address}
# ref.push(new_data)

app=Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    ref = db.reference("/restaurants/")    
    result=ref.get()
    return result
    #or return str(result)

if __name__ == '__main__':
    app.run(debug=True)