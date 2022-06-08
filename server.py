server.py
Who has access

System properties
Type
Text
Size
531 bytes
Storage used
531 bytes
Location
messaging app
Owner
me
Modified
18 Apr 2021 by me
Opened
09:16 by me
Created
18 Apr 2021 with Google Drive Web (Unverified)
Add a description
Viewers can download
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import sys
import time

s=socket.socket()
host=input(str("please enter the host you want to connect to"))
port=1025

try:
    s.connect((host.port))
    print("connected to host")
except:
    print("connection failed")
    
while 1:
    incoming_message=s.recv(1024)
    incoming_message = incoming_message.decode()
    print("reply", incoming_message)
    
    message=input(str("enter your message"))
    message=message.encode()
    s.send(message)


# In[ ]:



