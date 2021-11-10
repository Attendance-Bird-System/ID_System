from pyasn1.type.univ import Null
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

    def __init__(self ):        
        # initialize the fire base using credintials
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        
        # Get a reference to the auth service
        self.auth = firebase.auth() 

        # Get a reference to the database service
        self.db = firebase.database()
    
    def setuId(self , uId) :
        self.uId = uId 

    def SignUP(self, userMail , userPass , controller) :
        try : 
            user = self.auth.create_user_with_email_and_password(userMail,userPass)
            self.auth.send_email_verification(user['idToken']) # email sent ~~ 
            self.db.child( user['localId']).update(
                            {
                "data" : "NULL,NULL",
                "lastID" : "NULL,notFound",
                "nGroups" : 0,
            }, )
            
            messagebox.showinfo(f"email verificationl", "verification email sent to "+userMail)        
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))
        else :
            # Sign Up Sucessfully 
             # Write Initial Data to Firebase 
            controller.show_frame("SignInPage")


    def SignIn(self, userMail , userPass , rememberbox , controller) :
        try : 
            user = self.auth.sign_in_with_email_and_password(userMail,userPass)
            self.uId = user['localId']
            userVerified = self.auth.get_account_info(user['idToken'])['users'][0]['emailVerified'] 
            if userVerified : 
                # Sign in Sucessfully 
                if rememberbox :
                     with open("userData.birdInf" , 'w') as file :
                         file.write("remeber," + self.uId)
                       # navigate to the dashboard 
                controller.changesize()
                controller.show_frame("DashBoardPage")
            else :
                messagebox.showinfo("SignIN Error", "Please Verifiy your mail \n ather email will be sent now")
                self.auth.send_email_verification(user['idToken'])
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))
    
    def forgetPass(self , emailAddress , controller ) :
        try :
            self.auth.send_password_reset_email(emailAddress)   
            controller.show_frame("SignInPage")
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            messagebox.showinfo("SignUP Error", str(error))


fireBase = fireBaseControll()