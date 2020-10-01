import os
def file_remover():
	print ("File path:")
	a = input(">")
	print (a)
	os.remove(a)

file_remover()
