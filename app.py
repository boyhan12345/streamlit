import streamlit as st
import pandas as pd
st.title("나의 Streamlit 웹페이지")

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120)

if st.button("확인"):
    st.write(f"안녕하세요 {name}님, {age}살이시군요!")
col1, col2 = st.columns(2)

with col1:
    st.header("왼쪽")
    st.write("왼쪽 영역")

with col2:
    st.header("오른쪽")
    st.write("오른쪽 영역")
st.sidebar.title("메뉴")
menu = st.sidebar.selectbox(
    "이동",
    ["홈", "통계", "설정"]
)

if menu == "홈":
    st.write("홈 화면")
elif menu == "통계":
    st.write("통계 화면")
else:
    st.write("설정 화면")
df = pd.DataFrame({
    "월": ["1월", "2월", "3월"],
    "매출": [100, 150, 90]
})

st.bar_chart(df.set_index("월"))