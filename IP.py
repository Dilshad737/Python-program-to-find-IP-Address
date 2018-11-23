# Python Program to Get IP Address
# Developed by: DILSHAD ALI CHATTHA
# E-mail:       ghaznvi737@gmail.com
# GIT:          https://github.com/Dilshad737
# BLOG:         https://dilshad737.blogspot.com/
# MOB:          +923023331087

import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)  
