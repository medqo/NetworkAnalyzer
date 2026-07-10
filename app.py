import streamlit as st

from diagnosis import get_diagnosis
from analyzer import analyze_command
from checker import check_result
from recovery import get_recovery


st.set_page_config(
    page_title="Network Troubleshooting Assistant",
    layout="wide"
)


st.title("Network Troubleshooting Assistant")


# ==========================
# 障害選択
# ==========================

problem = st.selectbox(
    "発生している障害を選択",
    [
        "同一VLANなのに通信できない",
        "遠隔サイトへpingできない",
        "OSPF neighborが出ない"
    ]
)



# ==========================
# 原因候補表示
# ==========================

info = get_diagnosis(problem)


st.subheader("考えられる原因")


for layer, causes in info["causes"].items():

    st.write(f"### {layer}")

    for c in causes:
        st.write("- " + c)



# ==========================
# 確認コマンド
# ==========================

st.subheader("確認すべきコマンド")


command = st.selectbox(
    "Command",
    info["commands"]
)



# ==========================
# show結果入力
# ==========================

output = st.text_area(
    "showコマンド結果を貼付",
    height=250
)



# ==========================
# 解析
# ==========================


if st.button("Analyze"):


    parsed = analyze_command(
        command,
        output
    )


    result = check_result(
        command,
        parsed
    )


    st.subheader("診断結果")


    st.write(
        "Layer:",
        result["layer"]
    )


    st.write(
        "Problem:",
        result["problem"]
    )


    st.write(
        "Reason:",
        result["reason"]
    )



    st.subheader("Recovery Command")


    st.code(
        get_recovery(
            result["error"]
        )
    )