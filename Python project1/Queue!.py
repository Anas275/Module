def enqueue(a):
    item=int(input("Enter Number to Enqueue:"))
    a.append(item)
def dequeue(a):
    if len(a)==0:
       print("Queue Underflow:")
    else:
       item=a.pop(0)
       print("Dequeued Item=",item)
def peek(a):
    if len(a)==0:
        print("Queue Underflow:")
    else:
        item=a[0]
        print("Peek Item",item)
def display(a):
    if len(a)==0:
        print("Queue Underflow:")
    else:
        for i in range(0,len(a)):
            print(a[i])
a=[]
front=rear=None
while True:
    ch=int(input("1->Enqueue\n2->Dequeue\n3->Peek\n4->Display\n5->Exit\nEnter your choice: "))
    if ch==1:
        enqueue(a)
    elif ch==2:
        dequeue(a)
    elif ch==3:
        peek(a)
    elif ch==4:
        display(a)
    else:
        break

