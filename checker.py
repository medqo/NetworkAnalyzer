def check_result(command, result):


    # L1

    if result.get("interface_down"):

        return {

            "error":"interface_down",

            "layer":"L1",

            "problem":
            "Interface Down",

            "reason":
            "インターフェースが停止しています"

        }



    if result.get("shutdown"):

        return {

            "error":"router_down",

            "layer":"L1",

            "problem":
            "Router Interface Down",

            "reason":
            "Router側Interfaceがshutdown状態です"

        }



    # VLAN

    if result.get("vlan10") == False \
    or result.get("vlan20") == False \
    or result.get("vlan30") == False:


        return {

            "error":"vlan_missing",

            "layer":"L2",

            "problem":
            "VLAN Missing",

            "reason":
            "必要なVLAN10/20/30がありません"

        }



    # Trunk

    if result.get("allowed_vlan") == False:


        return {

            "error":"trunk_error",

            "layer":"L2",

            "problem":
            "Trunk VLAN Error",

            "reason":
            "TrunkでVLAN10/20/30が許可されていません"

        }



    # Router on Stick

    if result.get("subinterface") == False:


        return {

            "error":"subinterface_error",

            "layer":"L3",

            "problem":
            "Subinterface Error",

            "reason":
            "VLAN用Subinterfaceが不足しています"

        }



    if result.get("dot1q") == False:


        return {

            "error":"dot1q_error",

            "layer":"L3",

            "problem":
            "dot1Q Error",

            "reason":
            "VLANタグ設定が不足しています"

        }



    return {

        "error":"none",

        "layer":"OK",

        "problem":"正常",

        "reason":"問題は検出されませんでした"

    }