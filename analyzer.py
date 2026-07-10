def analyze_command(command, output):


    result = {}

    output_lower = output.lower()



    # =====================
    # Interface
    # =====================


    if command == "show interfaces status":


        result["interface_down"] = (

            "disabled" in output_lower

            or

            "notconnect" in output_lower

        )



    # =====================
    # VLAN
    # =====================


    elif command == "show vlan":


        result["vlan10"] = "10" in output

        result["vlan20"] = "20" in output

        result["vlan30"] = "30" in output



    # =====================
    # Trunk
    # =====================


    elif command == "show interfaces trunk":


        result["trunk"] = (

            "trunk" in output_lower

        )


        result["allowed_vlan"] = (

            "10,20,30" in output.replace(" ","")

        )



    # =====================
    # Router
    # =====================


    elif command == "show running-config":


        result["subinterface"] = (

            ".10" in output

            and ".20" in output

            and ".30" in output

        )



        result["dot1q"] = (

            "dot1Q 10" in output

            and "dot1Q 20" in output

            and "dot1Q 30" in output

        )



    elif command == "show ip interface brief":


        result["shutdown"] = (

            "administratively down"

            in output_lower

        )



    return result