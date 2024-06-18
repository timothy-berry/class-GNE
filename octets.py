ip_addr = "10.88.17.100"

print()
for octet in ip_addr.split("."):
    print(f"Octet: {octet}")
    print(f"Binary: {bin(int(octet))}")
    print()
