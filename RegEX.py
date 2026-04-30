"""Regular expression --> RegEx --> are patterns
used to match, search, validate and manipulate the text
#data science
#ML
#recursive
#Hcl
#shahul@telxsi.com
#charan@google.com
"""
import re
text = "I have a cat"
#find cat is present in above tex
#1.search(pattern,text)
print(re.search("cat",text))
#2.findall(pattern,text)-->returns a list with matching string
text2 = "cat mat bat"
#find all the letters having "at"
print(re.findall("at",text2))
text3 = "DS with python and ML"
#replace ML with machine learning
print(text3.replace("ML","machine learning"))
print(re.sub("ML","machine learning",text3))
#split():by default returns a list
#print(re.split(" ",text3))
text4 = "shahul@gmail.com"
#print(re.split("@",text4))
"""
^ --> starts with
$ --> ends with
* --> 0 or more
+ --> 1 or more
[] --> set of character --> [abc]
\d --> digits from 0-9
\w --> word character --> a-z,A-Z,0-9
\s --> space
"""
t1 = "my number is 98776654637"
t2 = "38773723 is my number"
#extract numeric data from above 2 texts
print(re.findall(r'\d+',t2))