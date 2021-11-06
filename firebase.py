from pyrebase import pyrebase 
import requests
import json
from tkinter import messagebox

class fireBaseControll : 
    
    firebaseConfig = {
        "apiKey": "AIzaSyB675SHqMS18BQpZIanNMFIKPBiug748kg",
    "authDomain": "id-system-e6f0d.firebaseapp.com",
    "databaseURL": "https://id-system-e6f0d-default-rtdb.firebaseio.com",
    "projectId": "id-system-e6f0d",
    "storageBucket": "id-system-e6f0d.appspot.com",
    "messagingSenderId": "964843778949",
    "appId": "1:964843778949:web:38aafc765df3279a270aec",
    "measurementId" : "G-Y72B1GRY6T"
    }

    def __init__(self):
        print("initialize fire base ")
        
        # initialize the fire base using credintials
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        
        # Get a reference to the auth service
        self.auth = firebase.auth() 

        # Get a reference to the database service
        self.db = firebase.database()
    
    def SignUP(self, userMail , userPass) :
        try : 
            user = self.auth.create_user_with_email_and_password(userMail,userPass)
            self.uId = user['localId']
            self.auth.send_email_verification(user['idToken']) # email sent ~~ 
            
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))
        else :
            # Sign Up Sucessfully 
            print(self.uId)

    def SignIn(self, userMail , userPass) :
        try : 
            user = self.auth.sign_in_with_email_and_password(userMail,userPass)
            self.uId = user['localId']
            userVerified = self.auth.get_account_info(user['idToken'])['users'][0]['emailVerified'] 
            if userVerified : 
                # Sign in Sucessfully 
                 print(self.uId)                
            else :
                messagebox.showinfo("SignIN Error", "Please Verifiy your mail")
                # self.auth.send_email_verification(user['idToken'])
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))
    
    def forgetPass(self , emailAddress) :
        try :
            self.auth.send_password_reset_email(emailAddress)        
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))
