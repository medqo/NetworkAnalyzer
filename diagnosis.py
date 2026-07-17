def get_diagnosis(problem):

    table = {

        # ==========================================
        # 同じVLAN内で通信できない
        # ==========================================

        "同じVLAN内の端末同士で通信できない": {

            "causes": {

                "L1": [
                    "ケーブル未接続",
                    "Interface Down"
                ],

                "L2": [
                    "VLAN未作成"
                ],

                "L3": [
                    "IP Address設定ミス",
                    "Subnet Mask設定ミス"
                ]
            },

            "steps": [

                {
                    "layer": "L1",
                    "device": "SW1",
                    "command": "show interfaces status"
                },

                {
                    "layer": "L2",
                    "device": "SW1",
                    "command": "show vlan"
                }
            ]
        },


        # ==========================================
        # 異なるVLAN間で通信できない
        # ==========================================

        "異なるVLAN間で通信できない": {

            "causes": {

                "L1": [
                    "ケーブル未接続",
                    "Interface Down"
                ],

                "L2": [
                    "VLAN未作成",
                    "Trunk設定ミス",
                    "Trunkの許可VLAN不足"
                ],

                "L3": [
                    "Subinterface不足",
                    "IEEE802.1Q設定不足",
                    "Subinterface Down"
                ]
            },

            "steps": [

                # L1
                {
                    "layer": "L1",
                    "device": "SW1",
                    "command": "show interfaces status"
                },

                # L2-1
                {
                    "layer": "L2",
                    "device": "SW1",
                    "command": "show vlan"
                },

                # L2-2
                {
                    "layer": "L2",
                    "device": "SW1",
                    "command": "show interfaces trunk"
                },

                # L3-1
                {
                    "layer": "L3",
                    "device": "R1",
                    "command": "show running-config"
                },

                # L3-2
                {
                    "layer": "L3",
                    "device": "R1",
                    "command": "show ip interface brief"
                }
            ]
        },


        # ==========================================
        # Router-on-a-Stick
        # ==========================================

        "Router-on-a-Stickが動作しない": {

            "causes": {

                "L1": [
                    "Router接続Interface Down"
                ],

                "L2": [
                    "Trunk設定ミス",
                    "Trunkの許可VLAN不足"
                ],

                "L3": [
                    "Subinterface不足",
                    "IEEE802.1Q設定不足",
                    "Subinterface Down"
                ]
            },

            "steps": [

                {
                    "layer": "L1",
                    "device": "SW1",
                    "command": "show interfaces status"
                },

                {
                    "layer": "L2",
                    "device": "SW1",
                    "command": "show interfaces trunk"
                },

                {
                    "layer": "L3",
                    "device": "R1",
                    "command": "show running-config"
                },

                {
                    "layer": "L3",
                    "device": "R1",
                    "command": "show ip interface brief"
                }
            ]
        }
    }

    return table[problem]