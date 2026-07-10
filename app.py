import streamlit as st

from diagnosis import get_diagnosis
from analyzer import analyze_command
from checker import check_result
from recovery import get_recovery


# ==========================
# ページ設定
# ==========================

st.set_page_config(
    page_title="ネットワーク診断アシスタント",
    layout="wide"
)


st.title("ネットワーク診断アシスタント")


st.write(
    """
    Cisco Router-on-a-Stick構成を対象としたVLAN / Trunk / Subinterface 障害解析ツールです。
    """
)


# ==========================
# 障害選択
# ==========================

st.header("1. 障害内容の選択")


problem = st.selectbox(
    "発生している障害を選択：",

    [
        "同一VLANなのに通信できない",

        "異なるVLAN間で通信できない",

        "Router-on-a-Stickが動作しない"
    ]
)



# ==========================
# 原因候補
# ==========================

info = get_diagnosis(problem)


st.header("2. 考えられる原因")


for layer, causes in info["causes"].items():


    st.subheader(layer)


    for cause in causes:


        st.write(
            "- " + cause
        )



# ==========================
# 確認コマンド
# ==========================


st.header("3. 確認すべきコマンド")

command = st.selectbox(

    "実行したshowコマンドを選択：",

    info["commands"]

)



st.info(
    f"""
    Cisco CLIで上記のコマンドを実行してください。

    実行結果を下の入力欄に貼り付けてください。
    """
)



# ==========================
# コマンド結果入力
# ==========================


st.header("4. コマンド実行結果")


output = st.text_area(

    "showコマンド結果：",

    height=300,


    placeholder=
"""
例:

Port        Mode
Fa0/7       trunk


Vlans allowed on trunk

10,20,30
"""

)



# ==========================
# 解析処理
# ==========================


if st.button(
    "分析開始"
):


    if output.strip() == "":


        st.warning(
            "コマンド実行結果を入力してください"
        )


    else:


        # --------------------------
        # show解析
        # --------------------------

        parsed = analyze_command(

            command,

            output

        )



        # --------------------------
        # 正常値比較
        # --------------------------

        result = check_result(

            command,

            parsed

        )



        # ==========================
        # 結果表示
        # ==========================


        st.header("5. 診断結果")



        if result["error"] == "none":


            st.success(
                "問題は検出されませんでした"
            )


        else:


            st.error(
                "ネットワーク障害を検出しました"
            )



        col1, col2 = st.columns(2)



        with col1:


            st.subheader("障害情報")


            st.write(
                "Layer：",
                result["layer"]
            )


            st.write(
                "問題：",
                result["problem"]
            )


            st.write(
                "原因：",
                result["reason"]
            )



        with col2:


            st.subheader(
                "復旧コマンド"
            )


            recovery_command = get_recovery(

                result["error"]

            )


            st.code(

                recovery_command,

                language="bash"

            )



# ==========================
# Footer
# ==========================


st.divider()


# st.caption(
#     "Router-on-a-Stick VLAN Troubleshooting Assistant"
# )