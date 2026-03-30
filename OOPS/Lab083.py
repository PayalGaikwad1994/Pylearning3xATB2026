class Password:
    def __init__(self,password):
        self.__password=password

    def get_password(self,auth):
        if auth:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_password(self,password):
        if len(password)>6:
            self.__password=password
            print("Set to correct",self.__password)
        else:
            print("Not allowed,weak password")

pwd=Password("Hacker123")
pwd.get_password(True)
pwd.set_password("Chima123")
