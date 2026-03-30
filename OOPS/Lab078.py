class VWOLogin:
    email=None
    password=None

    def __init__(self,email,password):
        self.email=email
        self.password=password

    def login_confirm(self):
        if self.password=="Pass123":
            print("Login Successful")
        else:
            print("Login Failed")


amit=VWOLogin("poyal1998@gmail.com","123")
amit.login_confirm()

amit2=VWOLogin("poyal1998@gmail.com","Pass123")
amit2.login_confirm()