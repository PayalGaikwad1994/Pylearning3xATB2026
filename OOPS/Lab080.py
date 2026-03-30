class VWOlogin:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login(self):
        if self.__email == "abc@Gmail.com" and self.__password=="123":
            print()
            print("Login Successful")
        else:
             print("Login Failed")


v1=VWOlogin("abc@Gmail.com","1234")
v1.login()

v2=VWOlogin("abc@Gmail.com","123")
v2.login()