import streamlit as st
import random

# --- Streamlit 앱 시작 ---
st.set_page_config(page_title="구구단 연습장", layout="centered")

st.title("⭐ 신나는 구구단 연습! ⭐")
st.subheader("곱셈 마스터가 되어보자!")

# 세션 상태 초기화 (처음 실행될 때만)
if 'question' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.session_state.question = None
    st.session_state.answer_correct = None
    st.session_state.correct_answer = None

# 새 문제 생성 함수
def generate_new_question():
    # 2단부터 9단까지
    dan = random.randint(2, 9)
    # 1부터 9까지 곱하는 수
    num = random.randint(1, 9)
    
    st.session_state.question = f"{dan} x {num}"
    st.session_state.correct_answer = dan * num
    st.session_state.answer_correct = None # 정답 여부 초기화

# 첫 실행 시 문제 생성
if st.session_state.question is None:
    generate_new_question()

# --- 현재 문제 표시 ---
col1, col2 = st.columns([1, 2])

with col1:
    st.metric(label="현재 점수", value=f"{st.session_state.score} 점")
    st.metric(label="푼 문제 수", value=f"{st.session_state.total_questions} 개")

with col2:
    st.markdown(f"## **문제:** `{st.session_state.question}` 은(는) 얼마일까요?")

st.write("---")

# --- 정답 입력 및 확인 ---

# 사용자 입력
user_answer = st.number_input("여기에 정답을 입력하고 엔터를 누르세요:", min_value=1, step=1, key="user_input")

# 정답 확인 버튼
if st.button("정답 확인!"):
    st.session_state.total_questions += 1
    
    # 정답 체크
    if user_answer == st.session_state.correct_answer:
        st.session_state.score += 1
        st.session_state.answer_correct = True
        st.success(f"🎉 **정답이에요!** {st.session_state.question} = {st.session_state.correct_answer}")
    else:
        st.session_state.answer_correct = False
        st.error(f"❌ **아쉽지만 틀렸어요.** 정답은 {st.session_state.correct_answer} 입니다.")
    
    # 다음 문제 버튼을 보여주기 위해 상태 업데이트
    st.session_state.show_next_button = True

st.write("")

# --- 다음 문제로 넘어가기 ---
if st.session_state.get('show_next_button', False):
    if st.button("👉 다음 문제 풀기"):
        generate_new_question()
        st.session_state.show_next_button = False # 버튼 숨김
        st.experimental_rerun() # 앱을 다시 실행하여 다음 문제와 입력창 초기화

st.write("---")
st.info("💡 **팁:** 정답을 입력하고 '정답 확인!' 버튼을 누른 다음, '다음 문제 풀기' 버튼을 눌러주세요.")
