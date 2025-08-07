import streamlit as st
import pandas as pd
import altair as alt

# 데이터 로드
file_path = 'countriesMBTI_16types.csv'
data = pd.read_csv(file_path)

# 데이터 전처리: 각 MBTI 유형별로 가장 높은 비율을 가진 국가를 찾음
max_values = data.drop(columns='Country').max()  # 각 MBTI 유형의 최대 값 찾기
max_countries = data.loc[data.drop(columns='Country').idxmax()]  # 최대 값이 있는 국가 찾기

# 시각화를 위한 데이터 준비
chart_data = pd.DataFrame({
    'MBTI Type': max_values.index,
    'Country': max_countries,
    'Percentage': max_values.values
})

# Altair 차트 생성
chart = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('MBTI Type', sort='-y'),
    y='Percentage',
    color='Country',
    tooltip=['MBTI Type', 'Country', 'Percentage']
).properties(
    title="가장 높은 비율을 가진 MBTI 유형별 국가"
)

# Streamlit 앱 구성
st.title('MBTI 성격 유형 분석')
st.write("각 MBTI 유형에 대해 가장 높은 비율을 가진 국가를 확인할 수 있습니다.")
st.altair_chart(chart, use_container_width=True)
