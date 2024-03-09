import tkinter as tk
from tkinter import filedialog
import socket

def main():
    home_sc_window = tk.Tk()
    home_sc_window.title("home screen")
    home_sc_window.title("main_sc")

    homeLBL = tk.Label(master=home_sc_window, text="home screen")
    homeLBL.grid(row=1, column=0)

    inf = "our program uses ipv4 inet services to send and encrypt data,5 but further use of blockchain can be done"
    inflbl = tk.Label(master=home_sc_window, text=inf)
    inflbl.grid(row=2, column=1)

    def next():
        home_sc_window.destroy()
        home_sc()

    nbtn = tk.Button(master=home_sc_window, text="NEXT", command=next)
    nbtn.grid(row=3, column=3)
    home_sc_window.mainloop()
def send():
    filename=send_sc=ip=filename="temp"

    send_sc = tk.Tk()
    send_sc.title("send")
    IP = socket.gethostbyname(socket.gethostname())

    def browse():
        global filename
        filename = filedialog.askopenfilename()
    def back():
        send_sc.destroy()
        main()

    LBL1 = tk.Label(master=send_sc, text=F"SEND DOCUMENTS:      YOUR IP {IP}")
    LBL1.grid(row=0, column=0)

    filelbl = tk.Label(master=send_sc, text="CHOOSE THE FILE")
    filelbl.grid(row=1, column=0)
    browse_ac = tk.Button(master=send_sc, text="BROWSE SYSTEM", command=browse)
    browse_ac.grid(row=1, column=1, pady=10)

    tip = tk.Label(master=send_sc, text="ENTER TARGET IP")
    tip.grid(row=2, column=0)

    ip = tk.Entry(master=send_sc, width=30)
    ip.grid(row=2, column=1)

    port = tk.Label(master=send_sc, text="ENTER THE PORT")
    port.grid(row=3, column=0)
    p = tk.Entry(master=send_sc, width=30)
    p.grid(row=3, column=1)

    def exe():
        ip_val = ip.get()
        p_val = p.get()
        filename_val=filename
        print(ip_val, filename_val, p_val)
        send_sc.destroy()


    execute = tk.Button(master=send_sc, text="next", command=exe)
    execute.grid(row=4, column=2)

    backb = tk.Button(master=send_sc, text="back", command=back)
    backb.grid(row=4, column=1, pady=10)
    send_sc.mainloop()
def recv():
    recv_sc = tk.Tk()
    recv_sc.title("receive")
    IP = socket.gethostbyname(socket.gethostname())

    RCLBL = tk.Label(master=recv_sc, text=f"RECEIVE MESSAGES         YOUR IP{IP}")
    RCLBL.grid(row=0, column=0)

    portl = tk.Label(master=recv_sc, text="PORT")
    portl.grid(row=1, column=0)

    port = tk.Entry(master=recv_sc, width=30, font=("Helvetica", 12), bg="lightgray", fg="black")
    port.grid(row=1, column=1)

    ips = tk.Label(master=recv_sc, text="SOURCE IP")
    ips.grid(row=2, column=0)

    ip = tk.Entry(master=recv_sc, width=30, font=("Helvetica", 12), bg="lightgray", fg="black")
    ip.grid(row=2, column=1)

    def next():
        portl_val = portl.get()
        ip_val = ip.get()
        recv_sc.destroy()
        print(portl_val, ip_val)

    def back():
        recv_sc.destroy()
        main()

    backb = tk.Button(master=recv_sc, text="back", command=back)
    backb.grid(row=3, column=1, pady=10)

    nex = tk.Button(master=recv_sc, text="NEXT", command=next)
    nex.grid(row=3, column=2)

    recv_sc.mainloop()


def home_sc():
    main_sc = tk.Tk()
    main_sc.title("main_sc")
    window_width = 400
    window_height = 300
    main_sc.geometry(f"{window_width}x{window_height}")

    def sendb():
        main_sc.destroy()
        send()

    def recvb():
        main_sc.destroy()
        recv()

    def homeb():
        main_sc.destroy()
        home_sc()

    send_button = tk.Button(master=main_sc, text="send", command=sendb)
    send_button.grid(row=2, column=1, pady=10)

    recv_button = tk.Button(master=main_sc, text="receive", command=recvb)
    recv_button.grid(row=2, column=2, pady=10)

    home_button = tk.Button(master=main_sc, text="back", command=homeb)
    home_button.grid(row=2, column=3, pady=10)

    main_sc.mainloop()
                                 

if __name__ == "__main__":
    main()