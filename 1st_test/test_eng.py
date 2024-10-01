import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic)
plt.rcParams['font.family'] = 'Malgun Gothic'  # 맑은 고딕 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지는 문제 방지

# Define Knowledge Space with prerequisite relations
G = nx.DiGraph()
# 지식 요소와 선행 관계 추가 (덧셈, 뺄셈, 곱셈, 나눗셈을 영어로)
G.add_edges_from([('Addition', 'Subtraction'), ('Subtraction', 'Multiplication'), ('Multiplication', 'Division')])

# 학생의 지식 상태를 시뮬레이션
student_knowledge = {'Addition', 'Subtraction'}  # 학생이 알고 있는 지식

# 노드 색상 설정 (학생이 알고 있는 지식은 파란색, 모르는 지식은 빨간색)
node_colors = ['lightblue' if node in student_knowledge else 'lightcoral' for node in G.nodes]

# 시각화
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10)
plt.title("Knowledge Space and Student's Knowledge")
plt.show()

# 간단한 분석 예시: 학습 경로 탐색
# Division까지 가기 위한 경로 찾기
print("학습 경로:", list(nx.all_simple_paths(G, source='Addition', target='Division')))
