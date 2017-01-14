#!/usr/bin/env python3
init = "Pick Episode. Copyright (C) 2017 Aalok S.\nThis program comes with ABSOLUTELY NO WARRANTY; for details see GNU GPLv3.\nThis is free software, and you are welcome to redistribute it under certain conditions."
print(init)
def getepi():
	print("This is a trivial script written by Aalok S. in 2017.\nDone watching the entire series and now can't decide which episode you want to watch? Use this script to help you decide!\nPython3.* required\nPlease halt if you are using an older version\nPress return to continue")
	choice = input()	
	if choice in ["y","Y",""]:
		import random
		seasons = input("How many seasons does this franchise have?\n")
		episodes = input("How many episodes per season?\n")

		seasons=int(seasons)
		episodes=int(episodes)

		list1 = list(range(1,seasons+1))
		list2 = list(range(1,episodes+1))

		random.shuffle(list1)
		random.shuffle(list2)
		s = list1[0]
		if s<10: s="0"+str(s)
		else: s=str(s)
		e = list2[0]
		if e<10: e="0"+str(e)
		else: e=str(e)

		print("\nYou shall watch s%se%s of this show."%(s,e))
	else: exit()

getepi()
