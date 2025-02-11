# src/recommendation/graph_manager.py
import networkx as nx

class TravelGraphManager:
    def __init__(self):
        self.graph = nx.Graph()
        self.build_graph()

    def build_graph(self):
        # 각 여행지 노드에 특징(feature)을 부여합니다.
        self.graph.add_node("Paris", features=["romantic", "culture", "history"])
        self.graph.add_node("Tokyo", features=["modern", "tech", "culture"])
        self.graph.add_node("Bali", features=["relaxation", "beach", "adventure"])
        self.graph.add_node("New York", features=["urban", "culture", "entertainment"])
        
        # (선택 사항) 여행지 간 유사도를 표현하는 에지(간선) 추가
        self.graph.add_edge("Paris", "Tokyo", weight=0.4)
        self.graph.add_edge("Paris", "Bali", weight=0.3)
        self.graph.add_edge("Tokyo", "New York", weight=0.5)
        self.graph.add_edge("Bali", "New York", weight=0.2)

    def get_recommendations(self, user_preferences: list) -> list:
        """
        각 노드의 feature와 사용자가 입력한 선호 키워드의 일치 개수를 계산해
        추천 점수를 산출합니다.
        """
        scores = {}
        for node, data in self.graph.nodes(data=True):
            features = data.get("features", [])
            match_count = len(set(user_preferences).intersection(features))
            scores[node] = match_count
        
        # 점수가 0보다 큰 여행지만 반환 (내림차순 정렬)
        sorted_nodes = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        recommendations = [node for node, score in sorted_nodes if score > 0]
        return recommendations