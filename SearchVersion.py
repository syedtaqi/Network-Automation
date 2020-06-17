Code by Taqi Raza
#search for c1941 version router. if it is then #print the statement
from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'taqi',
    'password': 'cisco',

}

net_connect = ConnectHandler(**cisco_router)
output = net_connect.send_command('show version')
print (output)

version_output = output.find('1941')

if version_output> 0 :
     c1941 = True
else:
     c1941 = False

router = True

if router:
    if c1941:
        print (' this is a 1941 router')
    else: 
        print( ' This is a router, but not 1941 router')
else:
    print ( ' Not a router ' )
