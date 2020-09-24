import os
def file_creator():
	print ("File name:")
	a = input(">")
	print (a)
	f = open(a, "w")
	f.close()
	return None
def folder_creator():
	print ("Folder name:")
	a = input(">")
	os.mkdir(a)
	return None
print("New File or Folder?. If you are done, type exit")
b = input(">")
print (b)
user_input = ""
while user_input != "exit" or user_input != "Exit":
	print("New File or Folder?. If you are done, type Exit")
	b = input(">")
	print (b)
	if user_input == file or user_input == File:
		file_creator()
	elif user_input == folder or user_input == Folder:
		folder_creator()
	else:
		pass
pass