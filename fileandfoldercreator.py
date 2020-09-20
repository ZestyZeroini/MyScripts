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
file_creator()
folder_creator()