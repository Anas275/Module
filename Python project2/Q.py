# # list1 = [12,32,65,26,80,10]
# # list1.sort()
# # print(list1)
# #
# # list1 = [12,32,65,26,80,10]
# # sorted(list1)
# # print(list1)
#
# list1 = [1,2,3,2,6,5,2,6,8,0,10]
# print(list1[::-2])
# print(list1[:3]+list1[3:])
#
#
# list1 =[1,2,3,4,5]
# print(list1[len(list1)-1])
#
# myList = [10,20,30,40]
# myList.append([50,60])
# print(myList)
# myList.extend([80,90])
# print(myList)
#
#
# myList = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(myList)):
#     if i%2 == 0:
#         print(myList[i])
#
# myList = [1,2,3,4,5,6,7,8,9,10]
# del myList [:5]
# print(myList)
#
# myList = [1,2,3,4,5,6,7,8,9,10]
# del myList [3:]
# print(myList)
#
# myList = [1,2,3,4,5,6,7,8,9,10]
# del myList [::2]
# print(myList)

# list1 = []
# print("How many numbers do you want to enter in the list")
# maximum = int(input())
# print("Enter a list of numbers: ")
# for i in range(0,maximum):
#     n =int(input())
#     list1.append(n)
# num = int(input("Enter the numbers to be searched: "))
#
# position = -1
# for i in range(0, len (list1)):
#     if list1[i] == num:
#      position = i+1
# if position == -1 :
#     print("Number",num,"is not present in the list")
# else:
#     print("Number,num","is present at",position+1,"position")


num1 = 4
num2 = 3
num3 = 2
c=6
# print(num1+num2+num3)
# print(num1)
# num1=num1**(num2+num3)
# print(num1)
print(num1**=num2+c)
