import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎲", layout="centered")


# 로또 번호에 따른 색상 반환 함수 (공식 색상 기준)
def get_ball_color(number):
  if 1 <= number <= 10:
    return "#fbc400"  # 노란색
  elif 11 <= number <= 20:
    return "#69c8f2"  # 파란색
  elif 21 <= number <= 30:
    return "#ff7272"  # 빨간색
  elif 31 <= number <= 40:
    return "#aaaaaa"  # 회색
  else:
    return "#b0d840"  # 초록색


# 세션 상태(Session State) 초기화: 최대 5개의 게임 히스토리를 유지하기 위함
if "history" not in st.session_state:
  st.session_state.history = []

# 화면 제목
st.title("🎲 로또 번호 생성기")

# "로또번호 생성" 버튼
if st.button("로또번호 생성"):
  # 1~45 사이의 숫자 중 중복 없이 6개 추출 후 오름차순 정렬
  numbers = sorted(random.sample(range(1, 46), 6))

  # 생성된 번호를 기록에 추가
  st.session_state.history.append(numbers)

  # 최대 5개까지만 유지되도록 관리 (초과 시 가장 오래된 기록 제거)
  if len(st.session_state.history) > 5:
    st.session_state.history.pop(0)

st.divider()

# 화면에 누적된 번호 출력 (최대 5게임)
if st.session_state.history:
  st.subheader("생성된 로또 번호 목록 (최대 5게임)")

  # 저장된 번호 목록을 순서대로 화면에 표시
  for idx, game in enumerate(st.session_state.history, 1):
    cols = st.columns([1, 6])
    with cols[0]:
      st.markdown(f"**{idx}게임**")

    with cols[1]:
      # HTML 태그를 한 줄로 간결하게 작성하여 렌더링 오류 방지
      ball_htmls = []
      for num in game:
        color = get_ball_color(num)
        ball_htmls.append(
            f"<span style='display:inline-block; width:35px; height:35px;"
            f" background-color:{color}; color:white; border-radius:50%;"
            f" text-align:center; line-height:35px; font-weight:bold;"
            f" font-size:14px; margin-right:6px;"
            f" box-shadow:1px 1px 3px rgba(0,0,0,0.2);'>{num}</span>"
        )
      st.markdown("".join(ball_htmls), unsafe_allow_html=True)
    st.write("")
else:
  st.info("버튼을 눌러 로또 번호를 생성해 보세요!")
