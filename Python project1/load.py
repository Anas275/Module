import pickle
file=open("write.txt","rb")
l=pickle.load(file)
print(l)