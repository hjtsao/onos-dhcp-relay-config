Tested in Ubuntu 16.04 and Ubuntu 18.04 with onos-1.15 and onos-2.2
You need to modify apparmor in order to use isc-dhcp-server in mininet host's namespace
```bash
sudo ln -s /etc/apparmor.d/usr.sbin.dhcpd /etc/apparmor.d/disable/
sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.dhcpd
sudo /etc/init.d/apparmor stop
sudo sed -i '30i /var/lib/dhcpd{,3}/dhcpclient* lrw,' /etc/apparmor.d/sbin.dhclient
sudo /etc/init.d/apparmor start
```

To run the mininet topology
```bash
sudo python topo.py
```
