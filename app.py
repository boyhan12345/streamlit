import streamlit as st
import pandas as pd

# ---------------------
# 데이터
# ---------------------
PM_DATA = {
    "SAMSUNG": {
        "SM-100": pd.DataFrame([
            {"No": 1, "점검항목": "청결", "점검기준": "30≤"},
            {"No": 2, "점검항목": "그리스", "점검기준": "주입"},
            {"No": 3, "점검항목": "평탄도", "점검기준": "30≤"},
        ])
    }
}

# ---------------------
# 사이드바
# ---------------------
st.sidebar.title("메뉴")
page = st.sidebar.radio(
    "이동",
    ["Dashboard", "PM Sheet"]
)

# ---------------------
# Dashboard
# ---------------------
if page == "Dashboard":
    st.title("📊 장비 점검 대시보드")
    st.metric("총 장비 수", 5)
    st.metric("PASS", 42)
    st.metric("FAIL", 3)

# ---------------------
# PM Sheet
# ---------------------
elif page == "PM Sheet":
    st.title("🛠 PM Sheet")

    maker = st.selectbox("Maker 선택", list(PM_DATA.keys()))
    model = st.selectbox("Model 선택", list(PM_DATA[maker].keys()))

    df = PM_DATA[maker][model].copy()

    st.subheader(f"{maker} / {model} 점검표")

    # 점검값 입력
    df["점검값"] = ""
    df["점검결과"] = ""
    df["조치사항"] = ""
    df["점검값2"] = ""
    df["점검결과2"] = ""

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed"
    )

    if st.button("저장"):
        st.success("점검표가 저장되었습니다.")
