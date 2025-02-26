from ipaddress import *
for mask in range(10, 32):
	net = ip_network('111.233.75.16' + '/' + str(mask), 0)
	if '111.233.75.0/' + str(mask) == str(net):
		print(len(list(net)))
		break