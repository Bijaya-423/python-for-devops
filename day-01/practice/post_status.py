open_ports = [22, 80, 443]
port = 22

if port in open_ports:
    print("Port is Open")
else:
    print("Port is closed")