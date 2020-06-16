import json
from napalm import get_network_driver

#Retrieving BGP information from multiple Routers (E-BGP/I-BGP)
listBGP_ = [192.168.122.70, 
            192.168.122.72, 
            192.168.122.74, 
            192.168.122.76,
            192.168.122.78
]
for ip_ in listBGP:
   print ( "connecting to " + str(ip_))
   driver = get_network_driver('ios')
   router_bgp = driver (ip_, 'taqi', 'cisco') 
   router_bgp.open()

   bgp_neighbors = router_bgp.get_bgp_neighbors()
   print (json.dumps(bgp_neighbors, indent=3))

    router_bgp.close()
