def get_recovery(error, details=None):


    # VLANごとのGateway
    gateways = {

        10:
        "192.168.10.254",

        20:
        "192.168.20.254",

        30:
        "192.168.30.254"
    }


    # ==========================================
    # L1
    # ==========================================

    if error == "interface_down":

        return {

            "steps":
"""
1. ケーブル接続を確認する
2. 使用するInterfaceを確認する
3. shutdown状態の場合はInterfaceを有効化する
4. Interface状態を再確認する
""",

            "commands":
"""
enable
configure terminal

interface FastEthernet01
no shutdown

end

show interfaces status
"""
        }


    # ==========================================
    # VLAN
    # ==========================================

    elif error == "vlan_missing":

        commands = []


        for vlan in details or []:

            commands.append(
f"""
vlan {vlan}
name VLAN{vlan}
"""
            )


        return {

            "steps":
"""
1. 不足しているVLANを確認する
2. VLANを作成する
3. VLAN一覧を再確認する
""",

            "commands":
"""
enable
configure terminal

""" + "\n".join(commands) + """

end

show vlan
"""
        }


    # ==========================================
    # Trunk
    # ==========================================

    elif error == "trunk_error":

        return {

            "steps":
"""
1. Trunk Interfaceを確認する
2. Trunkモードを設定する
3. VLAN10、20、30を許可する
4. Trunk状態を再確認する
""",

            "commands":
"""
enable
configure terminal

interface FastEthernet07

switchport mode trunk
switchport trunk allowed vlan 10,20,30

end

show interfaces trunk
"""
        }


    # ==========================================
    # Subinterface不足
    # ==========================================

    elif error == "subinterface_missing":

        commands = []


        for vlan in details or []:

            gateway = gateways.get(
                vlan
            )


            commands.append(
f"""
interface FastEthernet0/0.{vlan}
encapsulation dot1Q {vlan}
ip address {gateway} 255.255.255.0
"""
            )


        return {

            "steps":
"""
1. 不足しているSubinterfaceを確認する
2. Subinterfaceを作成する
3. dot1Qを設定する
4. Gateway用IPアドレスを設定する
5. Interface状態を再確認する
""",

            "commands":
"""
enable
configure terminal

""" + "\n".join(commands) + """

end

show ip interface brief
"""
        }


    # ==========================================
    # dot1Q不足
    # ==========================================

    elif error == "dot1q_missing":

        commands = []


        for vlan in details or []:

            commands.append(
f"""
interface FastEthernet0/0.{vlan}
encapsulation dot1Q {vlan}
"""
            )


        return {

            "steps":
"""
1. dot1Q設定が不足しているSubinterfaceを確認する
2. 対象Subinterfaceへ移動する
3. 正しいVLAN IDを設定する
4. 設定を再確認する
""",

            "commands":
"""
enable
configure terminal

""" + "\n".join(commands) + """

end

show running-config
"""
        }


    # ==========================================
    # Subinterface Down
    # ==========================================

    elif error == "subinterface_down":

        commands = []


        for vlan in details or []:

            commands.append(
f"""
interface FastEthernet0/0.{vlan}
no shutdown
"""
            )


        return {

            "steps":
"""
1. DownしているSubinterfaceを確認する
2. 対象Subinterfaceを有効化する
3. 親Interfaceの状態も確認する
4. Interface状態を再確認する
""",

            "commands":
"""
enable
configure terminal

""" + "\n".join(commands) + """

interface FastEthernet0/0
no shutdown

end

show ip interface brief
"""
        }


    # ==========================================
    # 正常
    # ==========================================

    return {

        "steps":
        "復旧作業は不要です",

        "commands":
        ""
    }