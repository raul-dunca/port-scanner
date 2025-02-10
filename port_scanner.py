import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid number of arguments!")
    sys.exit()
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")

try:
    for port in range(0,65535):
        print(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET=ipv4, SOCK_STREAM=port
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator; if port not open returns 1

        if result == 0:
            print(f"Port: {port} is open!")

        s.close()
    print(f"Time ended: {datetime.now()}")
except KeyboardInterrupt:
    print("\nExiting!")
    sys.exit()
except socket.gaierror:
    print("Hostname can't be resolved")
    sys.exit()
except socket.error:
    print("Can't connect to the server")
    sys.exit()