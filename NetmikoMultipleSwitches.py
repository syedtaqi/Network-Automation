
iosv_L2_s1 = {
        'device_type': 'cisco_ios',
        'host': '192.168.122.72',
        'username': 'taqi',
        'password': 'cisco',
}

iosv_L2_s2 = {
        'device_type' : 'cisco_ios',
        'host' : '192.168.122.73',
        'username' :'taqi',
        'password': 'cisco',
}

iosv_L2_s3 = {
        'device_type' : 'cisco_ios',
        'host' : '192.168.122.74',
        'username': 'taqi'
        'password' : 'cisco'
}

all_switches = [iosv_L2_s1, iosvL2_s2, iosv_L2_s3]

for switchesToronto in all_switches:
         net_connect = ConnectHandler(**switchesToronto)

                for n in range (2,21):
                         print "Creating Vlan" + str(n)
                        config_commands = ["vlan " + str(n), "name Python_Vlan " + str(n)]
                        output = net_connect.send_config_set(config_commands)
                        print(output)
