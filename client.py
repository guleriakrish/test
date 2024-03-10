import os
import socket
import threading

IP=socket.gethostbyname(socket.gethostname())
PORT=1234
ADDR=(IP,PORT)
SIZE=2028
FORMAT="utf-8"
SERVER_DATA_PATH="server_data"

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        data=client.recv(SIZE).decode(FORMAT)
        cmd,msg=data.split("@")
        if cmd=="OK":
            print(f"{msg}")
        elif cmd=="DISCONNECTED":
            print(f"{msg}")
            break
        i=input("> ")
        i=i.split(" ")
        cmd = i[0]

        if cmd=="HELP":
            print("sending")
            client.send(cmd.encode(FORMAT))
        elif cmd=="LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd=="LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd=="UPLOAD":
            path=i[1]
            with open(f"{path}", "r") as f:
                text=f.read()
            filename=path.split("/")[-1]
            send_data=f"{cmd}@{filename}@{text}"
            print(send_data)
            client.send(send_data.encode(FORMAT))
            
        elif cmd=="DELETE":
            client.send(f"{cmd}@{i[1]}".encode(FORMAT))
            
    print("[DISCONNECTED FROM THE SERVER]")
    client.close()




if __name__=="__main__":
    main()
