#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import Node
from mininet.link import TCLink

class MyTopo( Topo ):

    def __init__( self ):

        Topo.__init__( self )

        h1 = self.addHost('h1', ip='0.0.0.0', mac='ea:e9:78:fb:fd:01')
        h2 = self.addHost('h2', ip='10.0.2.3', mac='ea:e9:78:fb:fd:02')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s1, s2)


def run():
    topo = MyTopo()
    net = Mininet(topo=topo, controller=None, link=TCLink)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    net.start()

    print("=== Run DHCP server ===")
    dhcp = net.getNodeByName('h2')
    # dhcp.cmdPrint('service isc-dhcp-server restart &')
    dhcp.cmdPrint('/usr/sbin/dhcpd -4 -pf /run/dhcp-server-dhcpd.pid -cf ./dhcpd.conf h2-eth0')

    CLI(net)
    print("=== Killing DHCP server ===") 
    dhcp.cmdPrint("kill -9 `ps aux | grep h2-eth0 | grep dhcpd | awk '{print $2}'`")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
run()
