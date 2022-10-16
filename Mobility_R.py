#!usrbinenv python
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args)

    net = Mininet_wifi()

    info( Creating nodesn)
    h1 = net.addHost( 'h1', mac='000000000001', ip='10.0.0.18' )
    sta1 = net.addStation( 'sta1', mac='000000000002', ip='10.0.0.28', range='20' )
    sta2 = net.addStation( 'sta2', mac='000000000003', ip='10.0.0.38', range='20' )
    sta3 = net.addStation( 'sta3', mac='000000000004', ip='10.0.0.48', range='20' )
    sta4 = net.addStation( 'sta4', mac='000000000005', ip='10.0.0.58', range='20' )
    sta5 = net.addStation( 'sta5', mac='000000000006', ip='10.0.0.68', range='20' )
    sta6 = net.addStation( 'sta6', mac='000000000007', ip='10.0.0.78', range='20' )
    ap1 = net.addAccessPoint( 'ap1', ssid= 'ap1-ssid', mode= 'g', channel= '1', position='60,40,0', range='30' )
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ap2-ssid', mode= 'g', channel= '1', position='60,140,0', range='30' )
    ap3 = net.addAccessPoint( 'ap3', ssid= 'ap3-ssid', mode= 'g', channel= '1', position='120,140,0', range='30' )
    ap4 = net.addAccessPoint( 'ap4', ssid= 'ap4-ssid', mode= 'g', channel= '1', position='120,100,0', range='30' )
    ap5 = net.addAccessPoint( 'ap5', ssid= 'ap5-ssid', mode= 'g', channel= '1', position='80,100,0', range='30' )
    ap6 = net.addAccessPoint( 'ap6', ssid= 'ap6-ssid', mode= 'g', channel= '1', position='120,40,0', range='30' )
    c1 = net.addController( 'c1' )

    info( Configuring propagation modeln)
    net.setPropagationModel(model=logDistance, exp=4.5)

    info( Configuring wifi nodesn)
    net.configureWifiNodes()

    info( Associating and Creating linksn)
    net.addLink(ap1, h1)
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.addLink(ap5, ap6)

    if '-p' not in args
        net.plotGraph(max_x=170, max_y=170)

    net.startMobility(time=0, ac_method='ssf')
    net.mobility(sta1, 'start', time=10, position='60,20,0')
    net.mobility(sta1, 'stop', time=20, position='60,140,0')
    net.mobility(sta2, 'start', time=30, position='60,140,0')
    net.mobility(sta2, 'stop', time=40, position='120,140,0')
    net.mobility(sta3, 'start', time=50, position='120,140,0')
    net.mobility(sta3, 'stop', time=60, position='120,100,0')
    net.mobility(sta4, 'start', time=70, position='120,100,0')
    net.mobility(sta4, 'stop', time=80, position='80,100,0')
    net.mobility(sta5, 'start', time=90, position='80,100,0')
    net.mobility(sta5, 'stop', time=100, position='120,40,0')
    net.mobility(sta6, 'start', time=110, position='120,40,0')
    net.mobility(sta6, 'stop', time=120, position='140,20,0')
    net.stopMobility(time=130)

    info( Starting networkn)
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])

    info( Running CLIn)
    CLI( net )

    info( Stopping networkn)
    net.stop()

if __name__ == '__main__'
    setLogLevel( 'info' )
    topology(sys.argv)
