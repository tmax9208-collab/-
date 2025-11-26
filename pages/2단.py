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

st.write("---")

if not st.session_state.quiz_finished:
    # 사용자 입력
    user_answer = st.number_input(
        "여기에 정답을 입력하고 엔터를 누르세요:", 
        min_value=1, 
        step=1, 
        key=f"input_{st.session_state.current_index}" # 문제마다 키 변경
    )

    # 정답 확인 버튼
    if st.button("정답 확인 및 다음 문제!"):
        if correct_answer is not None:
            check_answer(user_answer, correct_answer)
            st.experimental_rerun() # 피드백을 보여주고 다음 문제로 넘어가기 위해 앱 재실행
    
    # 피드백 메시지 표시
    if st.session_state.feedback:
        if "정답이에요" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
    
    st.write("---")
    
    # 현재 점수 현황
    st.info(f"✨ **현재 점수:** {st.session_state.score}점 / {st.session_state.current_index}문제")

else:
    # --- 퀴즈 종료 화면 ---
    st.balloons()
    st.success("🏆 **대단해요! 2단 마스터 완료!** 🏆")
    st.markdown(f"## 최종 점수: **{st.session_state.score}점** / **{st.session_state.total_questions}문제**")
    
    if st.button("처음부터 다시 시작"):
        # 세션 상태 초기화 후 재실행
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.feedback = ""
        st.session_state.quiz_finished = False
        st.experimental_rerun()
