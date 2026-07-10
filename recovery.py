def get_recovery(error):


    recovery = {


"interface":{


"steps":
"""
1. 対象Interfaceを確認する
2. Interface設定モードへ移行する
3. shutdown状態を解除する
4. 再度Interface状態を確認する
""",


"commands":
"""
enable

configure terminal


interface FastEthernet0/1

no shutdown


end


show interfaces status
"""

},



"vlan_missing":{


"steps":
"""
1. VLAN設定モードへ移行する
2. 不足しているVLANを作成する
3. VLAN作成結果を確認する
""",


"commands":
"""
enable

configure terminal


vlan 10
 name VLAN10

vlan 20
 name VLAN20

vlan 30
 name VLAN30


end


show vlan
"""

},



"trunk_allowed_error":{


"steps":
"""
1. Trunk Interfaceを確認する
2. Interface設定モードへ移行する
3. Trunkを有効化する
4. VLAN10/20/30を許可する
5. Trunk状態を確認する
""",


"commands":
"""
enable

configure terminal


interface FastEthernet0/7


switchport mode trunk

switchport trunk allowed vlan 10,20,30


end


show interfaces trunk
"""

},




"subinterface_missing":{


"steps":
"""
1. Router設定モードへ移行する
2. VLAN用Subinterfaceを作成する
3. dot1Qタグを設定する
4. Gateway IPアドレスを設定する
5. 設定状態を確認する
""",


"commands":
"""
enable

configure terminal


interface GigabitEthernet0/0/0.30

encapsulation dot1Q 30

ip address 192.168.30.254 255.255.255.0

no shutdown


end


show running-config
"""

},




"dot1q_missing":{


"steps":
"""
1. 対象Subinterfaceを確認する
2. Subinterface設定へ移動する
3. VLANタグ(dot1Q)を設定する
4. 設定内容を確認する
""",


"commands":
"""
enable

configure terminal


interface GigabitEthernet0/0/0.30

encapsulation dot1Q 30


end


show running-config
"""

},




"gateway_error":{


"steps":
"""
1. PCのIP設定画面を開く
2. 所属VLANを確認する
3. 対応するDefault Gatewayを設定する
4. pingで疎通確認する
""",


"commands":
"""
Packet Tracer PC:

Desktop
↓
IP Configuration


VLAN10:
Default Gateway
192.168.10.254


VLAN20:
Default Gateway
192.168.20.254


VLAN30:
Default Gateway
192.168.30.254


確認:

ping <宛先IP>
"""

}

}


    return recovery.get(

        error,

        {

        "steps":"復旧作業は不要です",

        "commands":""

        }

    )