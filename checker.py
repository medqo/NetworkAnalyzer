def check_result(command, parsed):


    # L1

    if parsed.get("interface") == "down":


        return {

            "error":"interface_down",

            "layer":"L1",

            "problem":"Interface Down",

            "reason":
            "ポートが停止しています"

        }



    # VLAN

    if parsed.get("vlan20_exists") == False:


        return {

            "error":"vlan_missing",

            "layer":"L2",

            "problem":"VLAN Missing",

            "reason":
            "必要なVLANがありません"

        }




    # Trunk

    if parsed.get("allowed_vlan") == [10]:


        return {

            "error":"trunk_error",

            "layer":"L2",

            "problem":"Trunk VLAN Error",

            "reason":
            "VLAN20が許可されていません"

        }




    # Route

    if parsed.get("ospf_route") == False:


        return {

            "error":"route_missing",

            "layer":"L3",

            "problem":"Route Missing",

            "reason":
            "OSPF経路がありません"

        }




    # OSPF

    if parsed.get("neighbor") == False:


        return {

            "error":"ospf_error",

            "layer":"L3",

            "problem":"OSPF Neighbor Error",

            "reason":
            "Neighbor未形成"

        }



    return {

        "error":"none",

        "layer":"-",

        "problem":"正常",

        "reason":"問題なし"

    }