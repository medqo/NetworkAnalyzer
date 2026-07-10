def get_diagnosis(problem):


    table={


"同一VLANなのに通信できない":{


"causes":{


"L1":[
"ケーブル未接続",
"Interface shutdown"
],


"L2":[
"VLAN未作成",
"Access VLAN設定ミス"
],


"L3":[
"IPアドレス設定ミス",
"Subnet Mask不一致"
]

},


"steps":[

{"layer":"L1",
"command":"show interfaces status"},

{"layer":"L2",
"command":"show vlan"},

{"layer":"L3",
"command":"show running-config"}

]

},



"異なるVLAN間で通信できない":{


"causes":{


"L1":[
"Interface shutdown"
],


"L2":[
"Trunk設定ミス"
],


"L3":[
"Default Gateway設定ミス",
"dot1Q設定ミス"
]

},


"steps":[

{"layer":"L1",
"command":"show interfaces status"},

{"layer":"L2",
"command":"show interfaces trunk"},

{"layer":"L3",
"command":"show running-config"}

]

},



"Router-on-a-Stickが動作しない":{


"causes":{


"L1":[
"Router Interface Down"
],


"L2":[
"Trunk VLAN設定ミス"
],


"L3":[
"Subinterface不足",
"dot1Q不足"
]

},


"steps":[

{"layer":"L1",
"command":"show interfaces status"},

{"layer":"L2",
"command":"show interfaces trunk"},

{"layer":"L3",
"command":"show running-config"}

]

}

}


    return table[problem]