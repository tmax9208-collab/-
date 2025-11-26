안녕하세요! 초등학교 2학년 아이들이 구구단 2단을 집중적으로 연습할 수 있는 스트림릿 앱 코드를 만들어 드릴게요. 2단을 완벽하게 마스터할 수 있도록 1부터 9까지 순서대로 문제를 내도록 구성했습니다. 🚀

🔢 구구단 2단 연습 앱 (Streamlit)
이 코드를 복사해서 app.py 파일로 저장하세요.

app.py
Python

import streamlit as st
import random

# --- 고정된 구구단 (2단) 데이터 ---
# (곱해지는 수, 정답) 리스트: 2 x 1, 2 x 2, ..., 2 x 9
GUGUDAN_2_SET = [(2, i, 2 * i) for i in range(1, 10)] 

# --- Streamlit 앱 시작 ---
st.set_page_config(page_title="구구단 2단 마스터!", layout="centered")

st.title("✌️ 구구단 2단 마스터 도전! ✌️")
st.subheader("2단은 내가 제일 잘해!")

# 세션 상태 초기화
if 'current_index' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total_questions = len(GUGUDAN_2_SET) # 전체 문제 수 9개
    st.session_state.current_index = 0  # 현재 풀고 있는 문제의 인덱스 (0부터 시작)
    st.session_state.feedback = "" # 사용자 피드백 메시지
    st.session_state.quiz_finished = False # 퀴즈 종료 여부

# --- 문제 생성 및 표시 함수 ---
def display_current_question():
    if st.session_state.current_index < st.session_state.total_questions:
        # 현재 인덱스에 해당하는 문제 정보 가져오기
        dan, num, correct_answer = GUGUDAN_2_SET[st.session_state.current_index]
        
        # 화면에 문제 표시
        st.markdown(f"## **문제 {st.session_state.current_index + 1}/{st.session_state.total_questions}:** `{dan} x {num}` 은(는) 얼마일까요?")
        return correct_answer
    else:
        # 모든 문제를 다 풀었을 때
        st.session_state.quiz_finished = True
        return None

# --- 정답 확인 로직 ---
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = f"🎉 **정답이에요!** 2 x {st.session_state.current_index + 1} = {correct_answer}"
    else:
        st.session_state.feedback = f"❌ **아쉽지만 틀렸어요.** 정답은 {correct_answer} 입니다."
    
    # 다음 문제로 인덱스 이동
    st.session_state.current_index += 1

# --- 메인 앱 레이아웃 ---

correct_answer = display_current_question()
