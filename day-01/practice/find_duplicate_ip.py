ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]

seen = set()

for ip in ips:
    if ip in seen:
        print("Duplicate IP:", ip)
    else:
        seen.add(ip)
        