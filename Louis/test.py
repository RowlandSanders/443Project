import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

config = {

  "apiKey": "AIzaSyAbmjyY5Oolx-MQzJJBqLtzUu6Q5ObHCt8",
  "authDomain": "scentproductionsllc.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "projectId": "scentproductionsllc",
  "storageBucket": "scentproductionsllc.appspot.com",
  "messagingSenderId": "563963156196",
  "appId": "1:563963156196:web:715df1c22e35b0817ebef1",
  "measurementId": "G-Y197YY3QN5"
}

#JS config
# const firebaseConfig = {
#   apiKey: "AIzaSyAbmjyY5Oolx-MQzJJBqLtzUu6Q5ObHCt8",
#   authDomain: "scentproductionsllc.firebaseapp.com",
#   projectId: "scentproductionsllc",
#   storageBucket: "scentproductionsllc.appspot.com",
#   messagingSenderId: "563963156196",
#   appId: "1:563963156196:web:715df1c22e35b0817ebef1",
#   measurementId: "G-Y197YY3QN5"
# };

#Initialize reference variables and connection
default_app = firebase_admin.initialize_app(config)


# user = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")

# Start listing users from the beginning, 1000 at a time.
page = auth.list_users()
while page:
    for user in page.users:
        print('User: ' + user.uid)
    # Get next batch of users.
    page = page.get_next_page()

# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.
for user in auth.list_users().iterate_all():
    print('User: ' + user.uid)