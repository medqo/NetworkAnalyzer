def get_diagnosis(problem):

    table = {


        "同一VLANなのに通信できない":{

            "causes":{

                "L1":[
                    "Interface shutdown"
                ],

                "L2":[
                    "Access VLAN設定ミス",
                    "VLAN未作成"
                ]

            },


            "commands":[

                "show interfaces status",

                "show vlan"

            ]

        },



        "異なるVLAN間で通信できない":{

            "causes":{

                "L2":[
                    "Trunk設定ミス",
                    "Allowed VLAN不足"
                ],

                "L3":[
                    "Subinterface未設定",
                    "dot1Q設定ミス"
                ]

            },


            "commands":[

                "show interfaces trunk",

                "show running-config",

                "show ip interface brief"

            ]

        },



        "Router-on-a-Stickが動作しない":{


            "causes":{

                "L2":[
                    "Trunk未設定"
                ],

                "L3":[
                    "encapsulation dot1Q不足"
                ]

            },


            "commands":[

                "show running-config",

                "show interfaces trunk"

            ]

        }

    }


    return table[problem]