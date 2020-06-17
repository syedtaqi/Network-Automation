
#forloop1 
#Dictionary:

cisco_router = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'taqi',
    'password': 'cisco',

}

#prints keys
for key in cisco_router:
     print(key)

#prints values
for value in cisco_router.values:
     print(value)

#prints keys and values
for value1 in cisco_router.items():
     print(value1)
