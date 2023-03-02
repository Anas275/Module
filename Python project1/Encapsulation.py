# class student:
#     name = "ravi"
# obj = student()
# print(obj.name)

class student:
    __name = "ravi"
    def __init__(self):
         print(self.__name)
         self.__displayinfo()
    def __displayinfo(self):
        print("welcome to aayam")
obj = student()