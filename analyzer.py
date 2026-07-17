def analyze_command(command, output):


    result = {}


    text = output.lower()



    # ======================
    # L1
    # ======================


    if command == "show interfaces status":


        # 正しいポート割当

        expected_vlan = {

            "fa0/1": "10",

            "fa0/2": "10",

            "fa0/3": "20",

            "fa0/4": "20",

            "fa0/5": "30",

            "fa0/6": "30",

            "fa0/7": "trunk",

            "fa0/8": "trunk"

        }


        interface_ok = True

        vlan_assign_ok = True



        for line in text.splitlines():


            cols = line.split()


            if len(cols) < 3:

                continue



            port = cols[0]

            status = cols[1]

            vlan = cols[2]



            # 管理対象ポートのみ確認

            if port in expected_vlan:



                # =================
                # L1確認
                # =================


                if status != "connected":


                    interface_ok = False




                # =================
                # VLAN確認
                # =================


                if vlan != expected_vlan[port]:


                    vlan_assign_ok = False




        result["interface_ok"] = interface_ok


        result["vlan_assign_ok"] = vlan_assign_ok



    # ======================
    # VLAN
    # ======================


    elif command == "show vlan":


        result["vlan_ok"] = (

            "10" in text

            and

            "20" in text

            and

            "30" in text

        )



    # ======================
    # Trunk
    # ======================


    elif command == "show interfaces trunk":


        trunk_text = text.replace(
            " ",
            ""
        )


        result["trunk_ok"] = (

            "10,20,30"

            in trunk_text

        )



    # ======================
    # Router
    # ======================


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