#This isis python script is used to create nsap addresses.
#Ronim Aon

#!/usr/bin/env python3

import sys

ipAddress = sys.argv[1]

octets = ipAddress.split('.', 4)

netstring = '49.0001.'
ipString = ''
for octet in octets:
    ipString += octet.zfill(3)

n = 4
for i in range(0, len(ipString), n):
    netstring += ipString[i:i+n]
    netstring += '.'

netstring += '00'

print(netstring)
