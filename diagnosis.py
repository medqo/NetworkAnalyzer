def get_diagnosis(problem):


    common_l1 = [

        "ケーブル未接続",

        "Interface shutdown"

    ]



    table = {


    # ==========================
    # 同一VLAN通信不可
    # ==========================


    "同じVLAN内の端末同士で通信できない":{


        "causes":{


            "L1": common_l1,


            "L2":[

                "VLAN未作成",

                "Access VLAN割当ミス"

            ],


            "L3":[

                "IP Address設定ミス",

                "Subnet Mask不一致"

            ]

        },


        "steps":[


            {
                "layer":"L1",

                "device":"接続先Switch",

                "command":"show interfaces status"
            },


            {
                "layer":"L2",

                "device":"SW1 / SW2",

                "command":"show vlan"
            },


            {
                "layer":"L3",

                "device":"PC",

                "command":"ipconfig"
            }

        ]

    },



    # ==========================
    # VLAN間通信不可
    # ==========================


    "異なるVLAN間で通信できない":{


        "causes":{


            "L1":common_l1,


            "L2":[

                "Trunk設定ミス",

                "allowed VLAN不足"

            ],


            "L3":[

                "Router Subinterface不足",

                "IEEE802.1Q設定不足"

            ]

        },


        "steps":[


            {
                "layer":"L1",

                "device":"SW1",

                "command":"show interfaces status"
            },


            {
                "layer":"L2",

                "device":"SW1",

                "command":"show interfaces trunk"
            },


            {
                "layer":"L3",

                "device":"R1",

                "command":"show running-config"
            }

        ]

    },



    # ==========================
    # 特定VLANのみ不可
    # ==========================


    "特定のVLANだけ通信できない":{


        "causes":{


            "L1":common_l1,


            "L2":[

                "VLAN未作成",

                "Trunk許可漏れ"

            ],


            "L3":[

                "対象VLANのSubinterface不足"

            ]

        },


        "steps":[


            {
                "layer":"L1",

                "device":"SW1",

                "command":"show interfaces status"
            },


            {
                "layer":"L2",

                "device":"SW1",

                "command":"show interfaces trunk"
            },


            {
                "layer":"L3",

                "device":"R1",

                "command":"show running-config"
            }

        ]

    },



    # ==========================
    # Router-on-a-Stick
    # ==========================


    "Router-on-a-Stickが動作しない":{


        "causes":{


            "L1":common_l1,


            "L2":[

                "Trunk未設定",

                "allowed VLAN不足"

            ],


            "L3":[

                "Subinterface不足",

                "dot1Q設定不足"

            ]

        },


        "steps":[


            {
                "layer":"L1",

                "device":"SW1",

                "command":"show interfaces status"
            },


            {
                "layer":"L2",

                "device":"SW1",

                "command":"show interfaces trunk"
            },


            {
                "layer":"L3",

                "device":"R1",

                "command":"show running-config"
            }

        ]

    },



    # ==========================
    # Gateway
    # ==========================


    "Default Gatewayへpingできない":{


        "causes":{


            "L1":common_l1,


            "L2":[

                "VLAN割当ミス"

            ],


            "L3":[

                "Default Gateway設定ミス"

            ]

        },


        "steps":[


            {
                "layer":"L1",

                "device":"SW1",

                "command":"show interfaces status"
            },


            {
                "layer":"L2",

                "device":"SW1",

                "command":"show vlan"
            },


            {
                "layer":"L3",

                "device":"PC",

                "command":"ipconfig"
            }

        ]

    }


    }


    return table[problem]