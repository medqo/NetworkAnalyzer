def check_layer(layer, result):


    # ==========================================
    # L1
    # ==========================================

    if layer == "L1":


        if result.get(
            "interface_ok"
        ) is False:

            return {

                "error":
                "interface_down",

                "problem":
                "Interface Down",

                "reason":
                "通信に使用するInterfaceが接続状態になっていません",

                "details":
                None
            }


    # ==========================================
    # L2
    # ==========================================

    elif layer == "L2":


        # VLAN確認
        if result.get(
            "vlan_ok"
        ) is False:

            missing = result.get(
                "missing_vlans",
                []
            )


            return {

                "error":
                "vlan_missing",

                "problem":
                "VLAN設定エラー",

                "reason":
                f"VLAN {missing} が作成されていません",

                "details":
                missing
            }


        # Trunk確認
        if result.get(
            "trunk_ok"
        ) is False:

            missing = result.get(
                "missing_trunk_vlans",
                []
            )


            if missing:

                reason = (
                    f"TrunkでVLAN {missing} "
                    "が許可されていません"
                )


            else:

                reason = (
                    "Trunkが正常に設定されていません"
                )


            return {

                "error":
                "trunk_error",

                "problem":
                "Trunk設定エラー",

                "reason":
                reason,

                "details":
                missing
            }


    # ==========================================
    # L3
    # ==========================================

    elif layer == "L3":


        # Subinterface存在確認
        if result.get(
            "subinterface_ok"
        ) is False:

            missing = result.get(
                "missing_subinterfaces",
                []
            )


            return {

                "error":
                "subinterface_missing",

                "problem":
                "Subinterface設定エラー",

                "reason":
                f"VLAN {missing} 用のSubinterfaceがありません",

                "details":
                missing
            }


        # dot1Q確認
        if result.get(
            "dot1q_ok"
        ) is False:

            missing = result.get(
                "missing_dot1q",
                []
            )


            return {

                "error":
                "dot1q_missing",

                "problem":
                "IEEE802.1Q設定エラー",

                "reason":
                f"VLAN {missing} のdot1Q設定がありません",

                "details":
                missing
            }


        # Subinterface状態確認
        if result.get(
            "subinterface_status_ok"
        ) is False:

            down = result.get(
                "down_subinterfaces",
                []
            )


            missing = result.get(
                "missing_status_subinterfaces",
                []
            )


            if down:

                reason = (
                    f"VLAN {down} 用のSubinterfaceが "
                    "up/up状態ではありません"
                )


            else:

                reason = (
                    f"VLAN {missing} 用のSubinterfaceを "
                    "確認できません"
                )


            return {

                "error":
                "subinterface_down",

                "problem":
                "Subinterface Down",

                "reason":
                reason,

                "details":
                down or missing
            }


    # ==========================================
    # 正常
    # ==========================================

    return {

        "error":
        "none",

        "problem":
        "なし",

        "reason":
        "この診断項目は正常です",

        "details":
        None
    }