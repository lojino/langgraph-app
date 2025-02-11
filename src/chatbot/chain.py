# src/chatbot/chain.py
import os
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from utils.config import PERSONA_TRAVEL_EXPERT  # utils 폴더의 config.py에서 불러옴# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

class TravelChatChain:
    def __init__(self):
        # API KEY 정보로드
        # load_dotenv()

        # OpenAI LLM 초기화
        self.llm = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4o")
        
        # 페르소나와 사용자 정보를 포함하는 프롬프트 템플릿 구성
        self.prompt_template = PromptTemplate(
            input_variables=["persona", "mbti", "travel_preference", "chat_history"],
            template=(
                "{persona}\n"
                "사용자의 MBTI: {mbti}\n"
                "여행 선호도 (예: romantic, adventure 등): {travel_preference}\n"
                "지금까지의 대화 이력: {chat_history}\n\n"
                "위 정보를 바탕으로 사용자에게 적합한 여행지 추천과 여행 조언을 해주세요."
            )
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def generate_response(self, mbti: str, travel_preference: str, chat_history: str) -> str:
        response = self.chain.run(
            persona=PERSONA_TRAVEL_EXPERT,
            mbti=mbti,
            travel_preference=travel_preference,
            chat_history=chat_history
        )
        return response