import os

try:
    # print(os.system('cmd /k' "node addstudent.js"))
    print(os.system('cmd /k' "electron ./main.js"))
except:
    print("Hello")