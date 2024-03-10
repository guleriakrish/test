import os
import socket
import threading

IP=socket.gethostbyname(socket.gethostname())
PORT=1234
ADDR=(IP,PORT)
SIZE=2028
FORMAT="utf-8"
SERVER_DATA_PATH="server_data"

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr}") 
    conn.send("OK@Welcome to the FIle server".encode(FORMAT))

    while True:
        data=conn.recv(SIZE).decode(FORMAT)
        data=data.split("@")
        print(data)
        cmd=data[0]
        if cmd=="HELP":
            send_data="OK@"
            send_data+="LIST : List all the files from the server\n"
            send_data+="UPLOAD <path> : Upload a file to the server.\n"
            send_data+="DELETE <filename>: Delete a file from the server.\n"
            send_data+="LOGOUT : Disconnect from the server\n"
            send_data+="HELP: List all the commands.\n"

            conn.send(send_data.encode(FORMAT))
        elif cmd=="LOGOUT":
            break
        elif cmd=="LIST":
            filelist=os.listdir(SERVER_DATA_PATH)
            send_data="OK@"

            if len(filelist)==0:
                send_data+="The file directory is empty"
            else:
                send_data+="\n".join(f for f in filelist)
            conn.send(send_data.encode(FORMAT))
        elif cmd=="UPLOAD":
            name=data[1]
            text=data[2]
            filepath=os.path.join(SERVER_DATA_PATH, name)
            with open(filepath,"w") as f:
                f.write(text)
            send_data="OK@File Uploaded"
            conn.send(send_data.encode(FORMAT))
        elif cmd=="DELETE":
            filelist=os.listdir(SERVER_DATA_PATH)
            send_data="OK@"
            print(filelist)
            filename=data[1]
            print(filename)
            if len(filelist)==0:
                send_data+="The server directory is empty"
            else:
                if filename in filelist:
                    os.system(f"rm {SERVER_DATA_PATH}/{filename}")
                    send_data+="File deleted"
                else:
                    send_data+="File not found"
            conn.send(send_data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr}")


def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    print("[SERVER IS STARTING]")
    server.listen()
    print("[SERVER IS LISTENING]")

    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()





if __name__=="__main__":
    main()
