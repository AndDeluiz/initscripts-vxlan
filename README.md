# Description

The initscripts package contains basic system scripts used during a boot of the system. It also contains scripts which activate and deactivate most network interfaces.

This package extends initscripts package by supporting VXLAN interfaces.

You can choose to build an RPM package or just place these scripts in `/etc/sysconfig/network-scripts` on your RedHat/CentOS/Fedora system.

Sample configuration for a `vxlan` interface:

	TYPE=vxlan
	DEVICE=vxlan1
	VNI=1
	VXLAN_MODE=unicast
	BOOTPROTO=none
	ONBOOT=yes
	TTL=255
	PHYS_DEV=ens3
	LOCAL_ADDR=192.168.0.1
	REMOTE_ADDR=192.168.0.2
	IPADDR=192.168.255.1
	NETMASK=255.255.255.248
	OPTIONS="nolearning"

Currently it supports only unicast mode with one peer.

This is a fork from https://github.com/eugenepaniot/initscripts-vxlan.

# To Do

- [ ] Support multicast mode.
- [ ] Allow more than one remote address when using unicast mode.
