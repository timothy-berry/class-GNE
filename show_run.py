from netmiko import ConnectHandler
from datetime import datetime

# cisco1.bogus.com does not resolve, so use it as fictional domain
device = {
    "device_type": "cisco_xe",
    "host": "cisco1.bogus.com",
    "username": "jmorrow",
    "password": "aTGcTAcGAtCg",
}

start_time = datetime.now()
with ConnectHandler(**device) as nc:
    data = nc.send_command("show run")
    print(data)

# print(data)
end_time = datetime.now()
print(f"{end_time - start_time}")
