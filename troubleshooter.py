def check_layer(layer, result):


    # =====================
    # Layer1
    # =====================

    if layer == "L1":


        if result.get("interface_ok") == False:


            return {

                "error":"interface",

                "problem":
                "Interface Down",

                "reason":
                "Interfaceがshutdown状態、またはリンクがDownしています"

            }



    # =====================
    # Layer2
    # =====================


    elif layer == "L2":


        if "vlan_ok" in result:


            if result["vlan_ok"] == False:


                return {

                    "error":
                    "vlan_missing",

                    "problem":
                    "VLAN Missing",

                    "reason":
                    "必要なVLANが作成されていません"

                }



        if "trunk_ok" in result:


            if result["trunk_ok"] == False:


                return {

                    "error":
                    "trunk_allowed_error",

                    "problem":
                    "Trunk VLAN Error",

                    "reason":
                    "Trunkで必要なVLANが許可されていません"

                }



    # =====================
    # Layer3
    # =====================


    elif layer == "L3":


        if "subinterface_ok" in result:


            if result["subinterface_ok"] == False:


                return {

                    "error":
                    "subinterface_missing",

                    "problem":
                    "Subinterface Error",

                    "reason":
                    "RouterのSubinterface設定が不足しています"

                }



        if "dot1q_ok" in result:


            if result["dot1q_ok"] == False:


                return {

                    "error":
                    "dot1q_missing",

                    "problem":
                    "IEEE802.1Q Error",

                    "reason":
                    "dot1Q設定が不足しています"

                }



    return {

        "error":"none",

        "problem":"なし",

        "reason":"正常です"

    }