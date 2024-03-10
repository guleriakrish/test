from cryptography.fernet import Fernet
with open("key.key","rb") as k:
    key=k.read()
fernet=Fernet(key)

with open("test_e.mp4","rb") as e:
    original_c=e.read()
original=fernet.decrypt(original_c)
with open("output/test.mp4","wb") as m:
    m.write(original)
