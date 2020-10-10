# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import os

def call_server(): 
    print("Server Running Successfully ")
    command = "python server.py"  #The command needs to be a string
    os.system(command) #The command can also be passed as a string, instead of a variable

def call_nodejs():
    print("Node JS Running Successfully ")
    cd = "cd Desktop-UI/javascript/" 
    # os.system(cd)
    os.system("node addstudent1.js")
   

	# command2 = "python hello.py"  #The command needs to be a string
   # os.system(command) #The command can also be passed as a string, instead of a variable

if __name__ == "__main__": 
	# creating thread 
	t1 = threading.Thread(target=call_nodejs) 
	t2 = threading.Thread(target=call_server) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	# wait until thread 2 is completely executed 
	# t2.join() 
	# t1.join() 

	# both threads completely executed 
	print("Done!") 
