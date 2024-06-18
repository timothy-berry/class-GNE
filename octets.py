ip_addr = "10.88.17.100"

for octet in ip_addr.split("."):
    print(octet)
    print(bin(int(octet)))
