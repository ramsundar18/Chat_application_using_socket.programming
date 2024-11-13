import socket as s
import select as sel
import sys
host=''
port=9999
soc_list=[]
recv_buff=4896
def chat_server():
    serv_soc=s.socket(s.AF_INET, s.SOCK_STREAM) 
    serv_soc.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
    serv_soc.bind((host,port))
    serv_soc.listen(5)
    soc_list.append(serv_soc)

    print ("Chat Server Sarted, Listening on Port "+str(port))
    while True:
        read,write,error=sel.select(soc_list,[],[],0)
        for i in read:
            if i==serv_soc:
                socfd,addr=serv_soc.accept()
                soc_list.append(socfd)
                print ("Client "+str(addr)+" Connected via Port Number 9999")
                print("\n")
                broadcast(serv_soc,socfd,"{} entered Our Chatting Room \n".format(addr))
            else:
                try:
                    data=i.recv(recv_buff)
                    print(str(addr[0])+" :- "+ data.decode('utf-8'))
                    if data:
                        broadcast(serv_soc,socfd,"[{}] {}".format(i.getpeername(),data))
                        pass
                    else:
                        if i in soc_list:
                            soc_list.remove(i)
                            broadcast(serv_soc,socfd,"[{}] Left the Chat \n".format(i.getpeername()))
                except:
                    broadcast(serv_soc,socfd,"[{}] Left the Chat \n".format(i.getpeername()))

                    continue
        # plan exit strategy
    serv_soc.close()
def broadcast(server,client,msg):
    for i in soc_list:
        if i!=server and i!=client:
            try:
                i.send(msg)
                print(msg)
            except:
                i.close()
                if i in soc_list:
                    soc_list.remove(i)
if __name__=="__main__":
    try:
        chat_server()
    except KeyboardInterrupt:
        print("Server shut down.")
        sys.exit(0)
