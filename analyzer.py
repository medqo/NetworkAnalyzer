def analyze_command(command, output):


    result = {}



    # interface

    if command == "show interfaces status":


        if "disabled" in output:

            result["interface"] = "down"


        else:

            result["interface"] = "up"




    # VLAN

    elif command == "show vlan":


        result["vlan20_exists"] = (

            "20" in output

        )




    # Trunk

    elif command == "show interfaces switchport":


        if "10,20" in output:

            result["allowed_vlan"] = [
                10,20
            ]


        else:

            result["allowed_vlan"] = [
                10
            ]




    # Routing

    elif command == "show ip route":


        result["ospf_route"] = (

            "O " in output

        )




    # OSPF

    elif command == "show ip ospf neighbor":


        result["neighbor"] = (

            "FULL" in output

        )



    return result