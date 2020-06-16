
import json
from napalm import get_network_driver

driver = get_network_driver('ios')

TorontovL2 = driver (192.168.122.71, 'taqi', 'cisco')

## Connect to the switch
TorontovL2.open()

#retrieve facts
Get_ = TorontovL2.get_facts()
print (json.dumps(Get_, indent=3))

#retrieve arp table
arp_ = TorontovL2.get_arp_table()
print (json.dumps(arp_, indent=3))

#retrieve mac table
mac_ = TorontovL2.get_mac_table()
print(json.dumps(mac_, indent=3))

#retrieve interface information
intfs_ = TorontovL2.get_interfaces()
print(json.dumps(intfs_, indent=3))

#Retrieve BGP information
bgp_neighbors = TorontovL2.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=3))



for ip_ in listBGP:
    print ("connecting to " + str(ip_))
    driver = get_network_driver("ios")

TorontovL2.close()
