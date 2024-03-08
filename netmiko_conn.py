from netmiko import ConnectHandler

rtr1 = {
    "device_type": "juniper_junos",
    "host": "rtr1.domain.com",
    "username": "juniper",
    "password": "juniper123!",
}

# Establish Netmiko Connection and execute simple 'show' command
with ConnectHandler(**rtr1) as net_connect:
    output = net_connect.send_command("show version")
