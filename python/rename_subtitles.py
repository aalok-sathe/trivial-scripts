import os
init = "Rename Subtitles. Copyright (C) 2017 Aalok S.\nThis program comes with ABSOLUTELY NO WARRANTY; for details see GNU GPLv3.\nThis is free software, and you are welcome to redistribute it under certain conditions."
print(init)

dirs = os.listdir()
list1=[]
list2=[]

for item in dirs:
	if item[0] != ".":
		l=len(item)
		if item[(l)-3:(l)] in ["mkv","mp4","avi","mpeg","mov"]: list1.append(item[:l-4])
		elif item[(l)-3:(l)] in ["srt","sub"]: list2.append(item[:l-4])
		
print(list1,list2)
cwd=os.getcwd()

for i in range(len(list2)):
	os.rename(list2[i]+".srt",list1[i]+".srt")
