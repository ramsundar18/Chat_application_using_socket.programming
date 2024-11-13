import sys
import socket
import select as sel
soc_list=[sys.stdin]
def chat_client():
    if len(sys.argv)<3:
        print("Usage : Python3 {} hostname port".format(sys.argv[1]))
    host=sys.argv[1]
    port=int(sys.argv[2])
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host,port))
    except:
        print("Cannot Reach the {}:{}".format(host,port))
        sys.exit(-1)
    print("Connected To The Remote Host , You can start Sending Messages....")
    sys.stdout.write(" > ")
    sys.stdout.flush()
    while True:
        read,write,error=sel.select(soc_list,[],[])
        for sock in read:
            if sock ==s:
                data=s.recv(4896)
                if not data:
                    print("Disconnected")
                else:
                    sys.stdout.write(data.decode('utf-8'))
                    sys.stdout.write(" > ")
                    sys.stdout.flush()
            else:
                msg=sys.stdin.readline()
                s.send(msg.encode('utf-8'))
                sys.stdout.write(" > ")
                sys.stdout.flush()
if __name__=="__main__":
    chat_client()
