def push(a,val):
    a.append(val)
def pop(a):
    item=a.pop()
    print("Popped item",item)
def peek(a):
    last=len(a)-1
    print("Peek Element=",a[last])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
#__main()__
a=[]
while True:
    choice=int(input("1->Push\n2->Pop\n3->Peek\n4->Display\n5->Exit\nEnter Your Choice"))
    if choice == 1:
        val = int(input("Enter Number to Insert:"))
        push(a,val)
        print("Element Pushed Successfully...")
    elif choice == 2:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            pop(a)
    elif choice == 3:
        if len(a)==0:
            print("Stack Underflow")
        else:
            peek(a)
    elif choice == 4:
        if len(a)==0:
            print("Stack Underflow")
        else:
            display(a)
    else:
        break;