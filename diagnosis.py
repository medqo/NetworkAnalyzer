def get_diagnosis(problem):


    data = {


        "同一VLANなのに通信できない": {


            "causes": {

                "L1":[
                    "ケーブル未接続",
                    "Interface shutdown"
                ],

                "L2":[
                    "VLAN割当ミス",
                    "Trunk設定ミス"
                ]

            },


            "commands":[

                "show interfaces status",

                "show vlan",

                "show interfaces switchport"

            ]

        },



        "遠隔サイトへpingできない":{


            "causes":{

                "L1":[
                    "Router間リンク障害"
                ],

                "L3":[
                    "経路未学習",
                    "Routing設定ミス"
                ]

            },


            "commands":[

                "show ip route",

                "show ip interface brief"

            ]

        },



        "OSPF neighborが出ない":{


            "causes":{

                "L3":[

                    "Area不一致",

                    "network設定不足"

                ]

            },


            "commands":[

                "show ip ospf neighbor",

                "show running-config"

            ]

        }


    }


    return data[problem]