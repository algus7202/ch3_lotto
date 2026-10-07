import random
import streamlit as st

# 1. 세션 상태 초기화 (최대 5개의 게임 히스토리를 유지하기 위함)
if "history" not in st.session_state:
  st.session_state.history = []

# 화면 제목
st.title("🎲 로또 번호 생성기")

# 2. "로또번호 생성" 버튼
if st.button("로또번호 생성"):
  # 1~45 사이의 숫자 중 중복 없이 6개 추출 후 오름차순 정렬
  numbers = sorted(random.sample(range(1, 46), 6))

  # 생성된 번호를 기록에 추가
  st.session_state.history.append(numbers)

  # 최대 5개까지만 유지되도록 관리 (가장 오래된 기록 제거)
  if len(st.session_state.history) > 5:
    st.session_state.history.pop(0)

st.divider()

# 3. 화면에 누적된 번호 출력 (최대 5개)
if st.session_state.history:
  st.subheader("생성된 로또 번호 목록 (최대 5게임)")

  # 저장된 번호 목록을 최신 순서(또는 등록 순서)로 화면에 표시
  for idx, game in enumerate(st.session_state.history, 1):
    st.write(f"**{idx}게임:** {game}")
else:
  st.info("버튼을 눌러 로또 번호를 생성해 보세요!")