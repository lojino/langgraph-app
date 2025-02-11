# src/main.py
import streamlit as st
from dotenv import load_dotenv
from chatbot.chain import TravelChatChain
from recommendation.travel_recommender import TravelRecommender

load_dotenv()  # .env 로드

def main():
    st.title("Travel Chatbot with MBTI & Travel Style")

    mbti = st.text_input("당신의 MBTI를 입력하세요 (예: ENFJ):")
    travel_style = st.text_area("원하는 여행 방식을 자유롭게 작성해보세요 (예: '힐링 중심의 여행을 하고 싶어요')")

    # (Optional) 기존 대화 이력이 있다면 입력받을 수 있음
    chat_history = st.text_area("대화 이력 (있다면 입력):", height=150)

    if st.button("여행 조언 받기"):
        # 1) LangChain을 이용한 대화 생성
        chat_chain = TravelChatChain()
        response = chat_chain.generate_response(mbti, travel_style, chat_history)
        st.subheader("챗봇 응답:")
        st.write(response)
        
        # 2) 변경된 추천 로직 사용
        recommender = TravelRecommender()
        recommendations = recommender.recommend(mbti, travel_style)
        
        st.subheader("추천 여행지:")
        if recommendations:
            for rec in recommendations:
                st.write("- " + rec)
        else:
            st.write("선호도에 맞는 여행지를 찾지 못했습니다.")

if __name__ == "__main__":
    main()