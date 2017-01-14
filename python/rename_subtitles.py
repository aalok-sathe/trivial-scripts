import os

dirs = os.listdir()
list1=[]
list2=[]

for item in dirs:
	if item[0] != ".":
		l=len(item)
		if item[(l)-3:(l)] == "mkv": list1.append(item[:l-4])
		elif item[(l)-3:(l)] == "srt": list2.append(item[:l-4])
		
print(list1,list2)
cwd=os.getcwd()

for i in range(len(list2)):
	os.rename(list2[i]+".srt",list1[i]+".srt")
