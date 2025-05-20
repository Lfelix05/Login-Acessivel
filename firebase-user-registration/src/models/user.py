class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_email(self):
        # Simple email validation logic
        return "@" in self.email and "." in self.email

    def validate_password(self):
        # Simple password validation logic
        return len(self.password) >= 6

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }