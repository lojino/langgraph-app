# src/recommendation/travel_recommender.py
from recommendation.graph_manager import TravelGraphManager

# (예시) MBTI별 일반적인 선호 키워드를 매핑한 사전
MBTI_FEATURE_MAP = {
    "ISTJ": ["organized", "planning", "introverted"],
    "ISFJ": ["supportive", "introverted", "relaxation"],
    "INFJ": ["insightful", "creative", "introverted"],
    "INTJ": ["logical", "planning", "introverted"],
    "ISTP": ["adventure", "problem-solving", "introverted"],
    "ISFP": ["artistic", "nature", "introverted"],
    "INFP": ["romantic", "creative", "introverted"],
    "INTP": ["theoretical", "analytical", "introverted"],
    "ESTP": ["adventure", "social", "extroverted"],
    "ESFP": ["entertainment", "social", "extroverted"],
    "ENFP": ["creative", "extroverted", "culture"],
    "ENTP": ["innovative", "extroverted", "adventure"],
    "ESTJ": ["organized", "extroverted", "culture"],
    "ESFJ": ["supportive", "social", "extroverted"],
    "ENFJ": ["supportive", "social", "culture"],
    "ENTJ": ["leader", "extroverted", "planning"]
}

class TravelRecommender:
    def __init__(self):
        self.graph_manager = TravelGraphManager()

    def recommend(self, mbti: str, travel_style: str) -> list[str]:
        """
        mbti: 사용자 MBTI (예: "ENFJ")
        travel_style: 사용자 여행 방식에 대한 자유로운 텍스트 (예: "힐링 중심의 여행을 하고 싶어요")
        """
        # 1) MBTI에서 키워드 추출
        mbti_keywords = MBTI_FEATURE_MAP.get(mbti.upper(), [])

        # 2) 여행 스타일 문장을 간단히 파싱하여 키워드 추출 (예시: 매우 단순한 규칙 기반)
        style_keywords = self.parse_travel_style(travel_style)

        # 3) 최종적으로 합쳐진 user_preferences
        user_preferences = list(set(mbti_keywords + style_keywords))

        # 4) 그래프 매니저의 추천 로직으로 여행지 목록 반환
        recommendations = self.graph_manager.get_recommendations(user_preferences)
        return recommendations

    def parse_travel_style(self, travel_style: str) -> list[str]:
        """
        여행 스타일을 나타내는 사용자의 문장을 간단한 규칙/키워드로 파싱하는 함수.
        실제로는 LLM 또는 더 복잡한 NLP 로직을 적용할 수도 있음.
        """
        travel_style = travel_style.lower()

        extracted_features = []

        # 예: "힐링", "휴양", "여유" 등의 단어가 들어가면 "relaxation" 추가
        if any(kw in travel_style for kw in ["힐링", "휴양", "여유"]):
            extracted_features.append("relaxation")

        # 예: "도시", "문화" 등의 단어가 들어가면 "culture" 추가
        if any(kw in travel_style for kw in ["도시", "문화"]):
            extracted_features.append("culture")

        # 예: "해변", "바다" 등의 단어가 들어가면 "beach" 추가
        if any(kw in travel_style for kw in ["해변", "바다", "비치"]):
            extracted_features.append("beach")

        # 예: "역사", "유적" 등의 단어가 들어가면 "history" 추가
        if any(kw in travel_style for kw in ["역사", "유적"]):
            extracted_features.append("history")

        # 예: "모험", "액티비티" 등의 단어가 들어가면 "adventure" 추가
        if any(kw in travel_style for kw in ["모험", "액티비티", "스릴"]):
            extracted_features.append("adventure")

        # 필요에 따라 다양한 규칙이나 LLM-based 추출을 여기에 추가 가능
        return extracted_features