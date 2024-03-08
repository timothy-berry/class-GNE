from netmiko import ConnectHandler

rtr1 = {
    "device_type": "juniper_junos",
    "host": "rtr1.domain.com",
    "username": "juniper",
    "password": "juniper123!",
}
rtr2 = {
    "device_type": "juniper_junos",
    "host": "rtr2.domain.com",
    "username": "juniper",
    "password": "juniper123!",
}

for device in (rtr1, rtr2):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command("show version")
        print(output)
