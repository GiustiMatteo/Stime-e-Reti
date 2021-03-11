import socket as sck

def client():
    host = "0.0.0.0"
    port = 7000  
    listPSW = ['rossi','213','clim']
    
    c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)   

    msg = ms

    c.sendto(msg.encode(), (host, port))    

    data = c.recv(4096)    

    print(f"riceve: {data.decode()}") 

    msg = listPSW

    if msg == "exit":
        c.sendto(bytes(msg, 'utf-8'), (host, port))  
        print("connessione chiusa")
    else :
        break

    c.close()   


if __name__ == '__main__':
    client()
