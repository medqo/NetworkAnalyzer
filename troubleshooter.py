def check_layer(layer, result):


    # ==========================
    # L1
    # Interface確認
    # ==========================


    if layer == "L1":


        if result.get("interface_ok") == False:


            return {

                "error":
                "interface_down",

                "problem":
                "Interface Down",

                "reason":
                "Interfaceがshutdown状態、または物理リンクがDownしています"

            }



    # ==========================
    # L2
    # VLAN / Trunk
    # ==========================


    elif layer == "L2":



        # VLAN確認

        if "vlan_ok" in result:


            if result["vlan_ok"] == False:


                return {

                    "error":
                    "vlan_missing",

                    "problem":
                    "VLAN設定エラー",

                    "reason":
                    "必要なVLANが作成されていません"

                }



        # Trunk確認

        if "trunk_ok" in result:


            if result["trunk_ok"] == False:


                return {

                    "error":
                    "trunk_error",

                    "problem":
                    "Trunk VLAN Error",

                    "reason":
                    "Trunkで必要なVLANが許可されていません"

                }




    # ==========================
    # L3
    # Router / PC
    # ==========================


    elif layer == "L3":



        # Subinterface確認

        if "subinterface_ok" in result:


            if result["subinterface_ok"] == False:


                return {

                    "error":
                    "subinterface_missing",

                    "problem":
                    "Subinterface Error",

                    "reason":
                    "RouterのVLAN用Subinterfaceが不足しています"

                }



        # dot1Q確認

        if "dot1q_ok" in result:


            if result["dot1q_ok"] == False:


                return {

                    "error":
                    "dot1q_missing",

                    "problem":
                    "IEEE802.1Q Error",

                    "reason":
                    "SubinterfaceにVLANタグ(dot1Q)設定がありません"

                }



        # Default Gateway確認

        if "ip_ok" in result:


            if result["ip_ok"] == False:


                return {

                    "error":
                    "gateway_error",

                    "problem":
                    "Default Gateway Error",

                    "reason":
                    "PCのDefault Gateway設定が不足しています"

                }



    # ==========================
    # 正常
    # ==========================


    return {

        "error":
        "none",

        "problem":
        "なし",

        "reason":
        "正常です"

    }