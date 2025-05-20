from firebase_admin import credentials, initialize_app, firestore

class FirebaseService:
    def __init__(self):
        cred = credentials.Certificate("path/to/your/firebase/credentials.json")
        initialize_app(cred)
        self.db = firestore.client()

    def register_user(self, email, password, accessibility):
        user_data = {
            "email": email,
            "password": password,
            "accessibility": accessibility
        }
        self.db.collection("users").add(user_data)