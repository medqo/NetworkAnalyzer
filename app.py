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
症状からOSI参照モデルに基づいて
L1 → L2 → L3 の順に障害を切り分けます。
"""
)


# ==========================================
# Session State
# ==========================================

if "step" not in st.session_state:

    st.session_state.step = 0


if "problem" not in st.session_state:

    st.session_state.problem = None


if "history" not in st.session_state:

    st.session_state.history = []


if "finished" not in st.session_state:

    st.session_state.finished = False


if "final_result" not in st.session_state:

    st.session_state.final_result = None


# ==========================================
# 症状選択
# ==========================================

if st.session_state.step == 0:


    problem = st.selectbox(

        "発生している症状",

        [
            "同じVLAN内の端末同士で通信できない",

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

        st.session_state.final_result = None

        st.rerun()


# ==========================================
# 症状・原因候補
# ==========================================

if st.session_state.problem:


    info = get_diagnosis(
        st.session_state.problem
    )


    st.subheader(
        "発生している症状"
    )


    st.info(
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


    st.divider()


# ==========================================
# 診断履歴
# ==========================================

if st.session_state.history:


    st.subheader(
        "診断履歴"
    )


    for history in st.session_state.history:


        if history["error"] == "none":

            st.success(
                f'{history["layer"]}：正常'
            )


        else:

            st.error(
                f'{history["layer"]}：異常'
            )


        st.caption(
            history["command"]
        )


        st.write(
            history["reason"]
        )


    st.divider()


# ==========================================
# 現在の診断
# ==========================================

if (
    st.session_state.step > 0
    and
    not st.session_state.finished
):


    current = info["steps"][
        st.session_state.step - 1
    ]


    layer = current["layer"]

    device = current["device"]

    command = current["command"]


    # 同じLayerが複数ある場合の番号
    same_layer_steps = [

        step

        for step in info["steps"]

        if step["layer"] == layer
    ]


    current_layer_number = (

        [
            step["command"]

            for step in same_layer_steps
        ].index(command)

        + 1
    )


    if len(same_layer_steps) > 1:

        layer_title = (

            f"{layer} 診断 "
            f"（{current_layer_number}/"
            f"{len(same_layer_steps)}）"
        )

    else:

        layer_title = (
            f"{layer} 診断"
        )


    st.header(
        layer_title
    )


    st.info(
f"""
**{device} で以下のコマンドを実行してください。**

`{command}`
"""
    )


    output = st.text_area(

        "コマンド実行結果",

        height=250,

        key=(
            f"input_"
            f"{st.session_state.step}_"
            f"{command}"
        )
    )


    if st.button(
        "分析"
    ):


        if not output.strip():

            st.warning(
                "コマンド実行結果を入力してください"
            )


        else:


            parsed = analyze_command(
                command,
                output
            )


            result = check_layer(
                layer,
                parsed
            )


            st.session_state.history.append({

                "layer":
                layer,

                "command":
                command,

                "error":
                result["error"],

                "reason":
                result["reason"]
            })


            # 障害あり
            if result["error"] != "none":


                st.session_state.finished = True

                st.session_state.final_result = result

                st.rerun()


            # 正常
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


# ==========================================
# 障害検出結果
# ==========================================

if (
    st.session_state.finished
    and
    st.session_state.final_result
):


    result = (
        st.session_state.final_result
    )


    st.error(
        "障害を検出しました"
    )


    st.subheader(
        "障害内容"
    )


    st.write(
        result["problem"]
    )


    st.subheader(
        "原因"
    )


    st.write(
        result["reason"]
    )


    recovery = get_recovery(

        result["error"],

        result["details"]

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


# ==========================================
# 全診断正常
# ==========================================

if (
    st.session_state.finished

    and

    st.session_state.final_result is None

    and

    st.session_state.history
):


    st.success(
        "今回の診断項目では異常は検出されませんでした"
    )


    st.subheader(
        "確認済み項目"
    )


    for history in (
        st.session_state.history
    ):

        st.write(

            "✓ "

            + history["command"]

        )


    st.subheader(
        "その他の原因候補"
    )


    st.warning(
"""
今回の診断対象外となる以下の項目も確認してください。

・PCのIP Address設定

・Subnet Mask設定

・Default Gateway設定

・Access VLANの割当

・ACLなどの通信制御
"""
    )


# ==========================================
# Reset
# ==========================================

st.divider()


if st.button(
    "最初から診断"
):


    st.session_state.step = 0

    st.session_state.problem = None

    st.session_state.history = []

    st.session_state.finished = False

    st.session_state.final_result = None


    st.rerun()