from datetime import datetime             # creating object
obj_now = datetime.now()                  # printing the current date and time
print("Current date & time: ", obj_now)   # extracting and printing the current
print("Current hour =", obj_now.hour)     # hour, minute, second and microsecond
print("Current minute =", obj_now.minute)
print("Current second =", obj_now.second)
print("Current microsecond =", obj_now.microsecond)

import pywhatkit
pywhatkit.sendwhatmsg("+918979288129","Hello test Message",obj_now.hour,obj_now.minute+1)