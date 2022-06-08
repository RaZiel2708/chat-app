host (1).py
Who has access

System properties
Type
Text
Size
615 bytes
Storage used
615 bytes
Location
messaging app
Owner
me
Modified
18 Apr 2021 by me
Opened
09:10 by me
Created
18 Apr 2021 with Google Drive Web (Unverified)
Add a description
Viewers can download
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("your connection is starting on",host)
port = 1025

s.bind((host,port))
print("server is ready to accept")

s.listen(1)
connection, addr=s.accept()
print("connection established to address:", addr)

while 1:
    message=input(str("enter your message"))
    message=message.encode()
    connection.send(message)
    
    incoming_message=connection.recv(1024)
    incoming_message=incoming_message.decode()
    print("reply", incoming_message)


# In[ ]:


hello


# In[ ]:



