
#!/bin/python
import sys
Import Socket
From datetime Import DateTime

#define Target 
if len(sys.argv == 2:
       target = Socket.gethostbyname(sys.argv[1])
    else:
        Print("Invalid amount of Arguments.")
        Print("Syntax:Python3 scanner.py<IP>")

#banner
Print("-"*50)
Print("Scanning Target" + Target)
Print("Time Started:" + Str(Datetime.now))
Print("-"*50)

#Full Port Scan (1,65535)

try:   
        For Port in range (1,65535):
            S = Socket.socket(socket.AF_INET,
                Socket.sock_Stream)
                Socket.setdefaulttimeout(1)
#Return Error   
                Result=S.Connect_ex((target,port))
                if results = 0:
                print("Port{} is open.") (port1)
                S.close()

Except KeyboardInterrupt:
Print("/n Exiting program")
sys.exit()

Except Socket.gaierror:
print("Hostname could not be resolved.")
sys.exit()

Except Socket.error
print("Coulnd't Connect to Server.")
sys.exit()


#Kali Executable 
~/python# python3 scanner.py (IP to be enumerate goes here in kali script)
CTRL C Exits program. 