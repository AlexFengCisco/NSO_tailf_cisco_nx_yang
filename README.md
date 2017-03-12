  
### Create some New Yang model to NX-OS CLI model for VXLAN EVPN

Device OS version : NX OS 7.0(3)I4(5)

####Add the following CLI yang Model

    [alex 0001] nv overlay evpn 
    [alex 0002] fabric forwarding anycast-gateway-mac MAC.MAC.MAC
    [alex 0003] vn-segnment id inside vlan configuraation
    [alex 0004] vni id inside vrf context configuration
    [alex 0005] rd auto inside vrf context configuration (on construction...)
    [alex 0006] route target both auto inside vrf context address-family ipv4 unicast
                route target both auto evpn @same location
    [alex 0007] feature vn-segment-vlan-based
    [alex 0008] feature nv overlay
    [alex 0009] interface nve configuration (on construction...)

TO BE CONTINUE .....