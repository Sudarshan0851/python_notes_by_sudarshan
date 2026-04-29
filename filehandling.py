#what is  file handling?
#handling files except python file is known as file handling ex:-text,json,csv,excel,etc..
#to handle other files in python we use the "open(file name ,"mode")"
#while handling the files wee have 4 modes ---> x,w,a,r.
#1. x- mode is used to create a new file
"""f= open("text.txt","x")
f.close()
print("file created")"""
#2.w - mode to write or overwrite content in the file
"""f = open("text.txt","w")
f.write("hello ")
f.close()
"""
#3.a -- it is used to add or append extra content to the file
f = open("text.txt","a")
f.write(" sai pawar")
f.close()

#4.r -- it is used to read the file
f= open("text.txt","r")
print(f.read())
f.close()

#pickling :- the process of convert the file into bytes is known as pickling
#the process of converting the 2d data into 1d (bytes)is known as serialization
#the process of converting the 1d data into 2d is known as deserialization
#why we need to pickel the data ?
#to transferred over the network
#to build the ml models convert the file into the pickel
#serialisation
import pickle
l =[1,2,3,4,6,7,8,7,67,75,565,6]
print(type(l))
f = open ("text.pkl","wb")
pickle.dump(l,f)
f.close()
print("file serialized and saved")




