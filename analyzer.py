def analyze_command(command, output):


    result = {}

    # 全て小文字化
    text = output.lower()



    # =====================
    # L1
    # =====================

    if command == "show interfaces status":


        result["interface_ok"] = (

            "disabled" not in text

            and

            "notconnect" not in text

        )



    # =====================
    # L2 VLAN
    # =====================

    elif command == "show vlan":


        result["vlan_ok"] = (

            "10" in text

            and

            "20" in text

            and

            "30" in text

        )



    # =====================
    # L2 Trunk
    # =====================

    elif command == "show interfaces trunk":


        result["trunk_ok"] = (

            "10,20,30"

            in text.replace(" ","")

        )



    # =====================
    # L3 Router
    # =====================

    elif command == "show running-config":


        result["subinterface_ok"] = (

            ".10" in text

            and

            ".20" in text

            and

            ".30" in text

        )



        result["dot1q_ok"] = (

            "dot1q 10" in text

            and

            "dot1q 20" in text

            and

            "dot1q 30" in text

        )



    # =====================
    # PC
    # =====================

    elif command == "ipconfig":


        result["ip_ok"] = (

            "default gateway"

            in text

        )


    return result