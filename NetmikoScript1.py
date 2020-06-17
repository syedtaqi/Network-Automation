#!usr/bin/env python

from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
}

net_connect = ConnectHandler(**iosv_L2)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = [ "int loop 3", "ip address 3.3.3.3 255.255.255.0"]
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (2,21):
        print "Creating Vlan" + str(n)
        config_commands = ["vlan " + str(n), "name Python_Vlan " + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
        
