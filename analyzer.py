import re

from expected_config import EXPECTED


def analyze_command(command, output):

    result = {}

    # 大文字・小文字を統一
    text = output.lower()


    # ==========================================
    # L1
    # show interfaces status
    # ==========================================

    if command == "show interfaces status":

        connected_ports = []


        for line in text.splitlines():

            columns = line.split()


            if len(columns) < 2:

                continue


            port = columns[0]

            status = columns[1]


            # Interface行のみ対象
            if (
                port.startswith("fa")
                or
                port.startswith("gi")
            ):

                if status == "connected":

                    connected_ports.append(
                        port
                    )


        result["interface_ok"] = (
            len(connected_ports) > 0
        )


    # ==========================================
    # L2-1
    # show vlan
    # ==========================================

    elif command == "show vlan":

        found_vlans = []


        for vlan in EXPECTED["VLANS"]:

            pattern = (
                rf"^\s*{vlan}\s+"
            )


            if re.search(
                pattern,
                text,
                re.MULTILINE
            ):

                found_vlans.append(
                    vlan
                )


        missing_vlans = [

            vlan

            for vlan in EXPECTED["VLANS"]

            if vlan not in found_vlans
        ]


        result["vlan_ok"] = (
            len(missing_vlans) == 0
        )


        result["missing_vlans"] = (
            missing_vlans
        )


    # ==========================================
    # L2-2
    # show interfaces trunk
    # ==========================================

    elif command == "show interfaces trunk":

        # Trunk Interfaceの存在確認
        trunk_exists = (
            "trunking" in text
            or
            "trunk" in text
        )


        missing_vlans = []


        # VLAN許可リストを確認
        for vlan in EXPECTED["TRUNK_ALLOWED"]:

            vlan_pattern = (
                rf"\b{vlan}\b"
            )


            if not re.search(
                vlan_pattern,
                text
            ):

                missing_vlans.append(
                    vlan
                )


        result["trunk_ok"] = (

            trunk_exists

            and

            len(missing_vlans) == 0

        )


        result["missing_trunk_vlans"] = (
            missing_vlans
        )


    # ==========================================
    # L3-1
    # show running-config
    # ==========================================

    elif command == "show running-config":

        missing_subinterfaces = []

        missing_dot1q = []


        # Subinterface確認
        for vlan in EXPECTED["SUBINTERFACES"]:

            interface_pattern = (
                rf"^interface\s+\S+\.{vlan}\s*$"
            )


            if not re.search(
                interface_pattern,
                text,
                re.MULTILINE
            ):

                missing_subinterfaces.append(
                    vlan
                )


        # dot1Q確認
        for vlan in EXPECTED["DOT1Q"]:

            dot1q_pattern = (
                rf"^\s*encapsulation\s+dot1q\s+{vlan}\s*$"
            )


            if not re.search(
                dot1q_pattern,
                text,
                re.MULTILINE
            ):

                missing_dot1q.append(
                    vlan
                )


        result["subinterface_ok"] = (
            len(missing_subinterfaces) == 0
        )


        result["dot1q_ok"] = (
            len(missing_dot1q) == 0
        )


        result["missing_subinterfaces"] = (
            missing_subinterfaces
        )


        result["missing_dot1q"] = (
            missing_dot1q
        )


    # ==========================================
    # L3-2
    # show ip interface brief
    # ==========================================

    elif command == "show ip interface brief":

        down_subinterfaces = []

        missing_subinterfaces = []


        for vlan in EXPECTED["SUBINTERFACES"]:

            # VLAN番号に対応する行を検索
            pattern = (
                rf"^\S+\.{vlan}\s+.*$"
            )


            match = re.search(
                pattern,
                text,
                re.MULTILINE
            )


            # 行そのものが存在しない
            if not match:

                missing_subinterfaces.append(
                    vlan
                )

                continue


            line = match.group(0)

            columns = line.split()


            # 最後の2列が Status / Protocol
            if len(columns) >= 2:

                status = columns[-2]

                protocol = columns[-1]


                if not (
                    status == "up"
                    and
                    protocol == "up"
                ):

                    down_subinterfaces.append(
                        vlan
                    )


        result["subinterface_status_ok"] = (

            len(down_subinterfaces) == 0

            and

            len(missing_subinterfaces) == 0
        )


        result["down_subinterfaces"] = (
            down_subinterfaces
        )


        result["missing_status_subinterfaces"] = (
            missing_subinterfaces
        )


    return result