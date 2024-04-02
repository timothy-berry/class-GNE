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
nyc1 = {
    "device_type": "cisco_nxos",
    "host": "rtr1-nyc.domain.com",
    "username": "cisco",
    "password": "cisco!123!",
}

for device in (rtr1, rtr2, nyc1):
    # Establish Netmiko Connection and execute simple 'show' command
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command("show version")
        print(output)
