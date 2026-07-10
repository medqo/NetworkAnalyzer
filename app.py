import streamlit as st

from diagnosis import get_diagnosis
from analyzer import analyze_command
from troubleshooter import check_layer
from recovery import get_recovery


st.set_page_config(
    page_title="ネットワーク診断アシスタント",
    layout="wide"
)


st.title(
    "ネットワーク診断アシスタント"
)


st.write(
"""
症状を選択し、OSI参照モデルに基づいて
L1 → L2 → L3 の順番で障害を切り分けます。
"""
)



# ======================
# Session
# ======================

if "step" not in st.session_state:
    st.session_state.step = 0


if "problem" not in st.session_state:
    st.session_state.problem = None


if "history" not in st.session_state:
    st.session_state.history = []


if "finished" not in st.session_state:
    st.session_state.finished = False



# ======================
# 症状選択
# ======================

if st.session_state.step == 0:


    problem = st.selectbox(

        "発生している症状",

        [
            "同一VLANなのに通信できない",

            "異なるVLAN間で通信できない",

            "Router-on-a-Stickが動作しない"
        ]

    )



    if st.button(
        "診断開始"
    ):


        st.session_state.problem = problem

        st.session_state.step = 1

        st.session_state.history = []

        st.session_state.finished = False


        st.rerun()



# ======================
# 原因候補表示
# ======================


if st.session_state.problem:


    info = get_diagnosis(
        st.session_state.problem
    )


    st.subheader(
        "考えられる原因"
    )


    cols = st.columns(3)


    for i, layer in enumerate(
        ["L1", "L2", "L3"]
    ):


        with cols[i]:


            st.write(
                f"### {layer}"
            )


            for cause in info["causes"][layer]:


                st.write(
                    "- " + cause
                )



# ======================
# 診断履歴
# ======================


if st.session_state.history:


    st.subheader(
        "診断履歴"
    )


    for h in st.session_state.history:


        if h["error"] == "none":


            st.success(
                f'{h["layer"]} 正常'
            )


        else:


            st.error(
                f'{h["layer"]} 異常'
            )


        st.write(
            "結果:",
            h["reason"]
        )



# ======================
# 現在Layer診断
# ======================


if (
    st.session_state.step > 0

    and

    not st.session_state.finished
):


    current = (

        info["steps"]

        [st.session_state.step - 1]

    )


    layer = current["layer"]

    command = current["command"]



    st.divider()


    st.header(
        f"{layer} 診断"
    )



    st.info(
        f"確認コマンド：{command}"
    )



    # ======================
    # コマンド単位で入力管理
    # ======================

    output = st.text_area(

        "コマンド結果",

        height=250,


        key=f"input_{command}"

    )



    if st.button(
        "分析"
    ):


        parsed = analyze_command(

            command,

            output

        )



        result = check_layer(

            layer,

            parsed

        )



        # ======================
        # 履歴保存
        # ======================


        st.session_state.history.append(


            {

                "layer": layer,

                "command": command,

                "error": result["error"],

                "reason": result["reason"]

            }

        )



        # ======================
        # 異常検出
        # ======================


        if result["error"] != "none":


            st.session_state.finished = True


            st.error(
                "障害を検出しました"
            )


            # ======================
            # 障害内容
            # ======================

            st.subheader(
                "障害内容"
            )


            st.write(
                result["problem"]
            )



            # ======================
            # 原因
            # ======================


            st.subheader(
                "原因"
            )


            st.write(
                result["reason"]
            )



            # ======================
            # 復旧
            # ======================


            recovery = get_recovery(
                result["error"]
            )


            st.subheader(
                "復旧手順"
            )


            st.write(
                recovery["steps"]
            )



            st.subheader(
                "コマンド例"
            )


            st.code(

                recovery["commands"],

                language="bash"

            )



        # ======================
        # 正常
        # ======================


        else:


            if (

                st.session_state.step

                <

                len(info["steps"])

            ):


                st.session_state.step += 1



            else:


                st.session_state.finished = True



            st.rerun()



# ======================
# 全Layer正常
# ======================


if (

    st.session_state.finished

    and

    st.session_state.history

    and

    st.session_state.history[-1]["error"] == "none"

):


    st.success(

        "L1 / L2 / L3 の主要設定は正常です"

    )



    st.info(
"""
確認した範囲では問題は検出されませんでした。

その他の原因候補:

- IPアドレス設定ミス
- Subnet Mask不一致
- Default Gateway設定ミス
- Firewall
- ACL設定
"""
    )



# ======================
# Reset
# ======================


st.divider()


if st.button(
    "最初から診断"
):


    st.session_state.step = 0

    st.session_state.problem = None

    st.session_state.history = []

    st.session_state.finished = False


    st.rerun()