from ipaddress import *
net=ip_network('10.48.96.0/255.255.240.0')
print(bin(255)[2:].zfill(8)+bin(255)[2:].zfill(8)+bin(240)[2:].zfill(8)+bin(0)[2:].zfill(8),f'{net[0]:b}',f'{net[90]:b}',f'{net[-1]:b}',sep='\n')
k=0
for ip in net:
    #print('ip = ', ip)

    b=f'{ip:b}'
    #print('b = ', b)
    if b.count('1')>b.count('0'):
        k+=1
print(k)
from ipaddress import ip_network
net=ip_network('192.168.240.0/255.255.255.0')
print(f'{net[0]:b}'.count('1'))
k=0
for ip in net:
    b=f'{ip:b}'
    if b.count('1')==b.count('0'):
        k+=1
print(k)
from ipaddress import *
for mask in range(32,-1,-1):
    net1=ip_network(f'165.112.200.70/{mask}',0)
    net2=ip_network(f'165.112.175.80/{mask}',0)
    print(net1,net2)
    if net1==net2:
        print(mask)
        break
print(bin(158)[2:].zfill(8)+bin(116)[2:].zfill(8)+bin(11)[2:].zfill(8)+bin(146)[2:].zfill(8))
print(bin(158)[2:].zfill(8)+bin(116)[2:].zfill(8)+bin(0)[2:].zfill(8)+bin(0)[2:].zfill(8))
for mask in range(0,32):
    net=list(ip_network(f'158.116.11.146/{mask}',0))
    print(net)
