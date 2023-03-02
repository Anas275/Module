# l=[10,20,30,40]
# print(len(l))
#
# s = "welcome"
# print(len(s))


# class a:
#     def displayinfo(self, name = ' '):
#      print("welcome to aayam" + name)
# obj = a()
# obj.displayinfo()
# obj.displayinfo(' python')


# class a:
#     def displayinfo(self):
#      print("welcome to aayam")
# class b(a):
#     def displayinfo(self):
#      print("welcome to sikar")
# obj = b()
# obj.displayinfo()

# class a:
#     def displayinfo(self):
#      print("welcome to aayam")
# class b(a):
#     def displayinfo(self):
#      super().displayinfo()
#      print("welcome to sikar")
# obj = b()
# obj.displayinfo()

class area:
    def find_area(self, x=None, y=None):
     if x!= None and y!= None:
       print(x*y)
     elif x!=None:
       print(x*x)
     else:
         print("nothing")
obj = area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)
