def get_recovery(error):


    recovery = {


        "interface_down":

"""
interface fa0/x
 no shutdown
""",



        "router_down":

"""
interface gig0/0/0

no shutdown
""",



        "vlan_missing":

"""
vlan 10
vlan 20
vlan 30
""",



        "trunk_error":

"""
interface fa0/7

switchport mode trunk

switchport trunk allowed vlan 10,20,30
""",



        "subinterface_error":

"""
interface gig0/0/0.10

encapsulation dot1Q 10

ip address 192.168.10.254 255.255.255.0
""",



        "dot1q_error":

"""
interface gig0/0/0.10

encapsulation dot1Q 10
"""

    }


    return recovery.get(
        error,
        "修正不要"
    )