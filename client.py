from cryptography.fernet import Fernet
# import socket
# IP=socket.gethostbyname(socket.gethostname)
# PORT=1234
# ADDR=(IP,PORT)
# SIZE=1024
# FORMAT="utf-8"
#
# c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# c.connect(ADDR)
# print("[CONNECTED]")

key=Fernet.generate_key()
with open('key.key','wb') as filekey:
    filekey.write(key)
fernet=Fernet(key)

with open('test.mp4','rb') as file:
    original=file.read()

original_c=fernet.encrypt(original)
with open('test_e.mp4','wb') as file:
    file.write(original_c)



# msg=c.recv(SIZE).decode(FORMAT)
# print(f"[SERVER] {msg}")
#
