def get_recovery(error):


    recovery = {


        "interface_down":

"""
interface gi0/1
 no shutdown
""",


        "vlan_missing":

"""
vlan 20
 name VLAN20
""",


        "trunk_error":

"""
interface gi0/1

switchport mode trunk

switchport trunk allowed vlan 10,20
""",



        "route_missing":

"""
router ospf 1

network 192.168.0.0 0.0.255.255 area 0
""",



        "ospf_error":

"""
show running-config

OSPF area と network設定を確認
"""


    }



    return recovery.get(
        error,
        "No recovery needed"
    )