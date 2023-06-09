import pandas as pd
import matplotlib.pyplot as plt

# 단계별 입력값 받기
steps = ['메인화면', '로그인', '검색창', '제품 상세페이지', '제품 구매페이지', '결제페이지', '결제완료 페이지']
user_counts = []

for step in steps:
    while True:
        try:
            user_count = int(input(f'{step}의 사용자 수를 입력하세요: '))
            if len(user_counts) > 0 and user_count > user_counts[-1]:
                raise ValueError("이전 단계보다 큰 값이 입력되었습니다.")
            user_counts.append(user_count)
            break
        except ValueError as e:
            print(f"오류: {e}")
            exit(1)  # 오류 발생 시 프로그램 종료

# 데이터 프레임 생성
df = pd.DataFrame({'단계': steps, '사용자 수': user_counts})

# 전환율 계산
df['전환율'] = df['사용자 수'] / df['사용자 수'].iloc[0] * 100

# 이탈율 계산
df['이탈율'] = 100 - df['전환율'].cumsum()

# 단계별 사용자 수 시각화
plt.figure(figsize=(8, 6))
plt.bar(df['단계'], df['사용자 수'])
plt.xlabel('단계')
plt.ylabel('사용자 수')
plt.title('단계별 사용자 수')
plt.show()

# 단계별 전환율 시각화
plt.figure(figsize=(8, 6))
plt.plot(df['단계'], df['전환율'], marker='o')
plt.xlabel('단계')
plt.ylabel('전환율 (%)')
plt.title('단계별 전환율')
plt.grid(True)
plt.show()

# 단계별 이탈율 시각화
plt.figure(figsize=(8, 6))
plt.plot(df['단계'], df['이탈율'], marker='o')
plt.xlabel('단계')
plt.ylabel('이탈율 (%)')
plt.title('단계별 이탈율')
plt.grid(True)
plt.show()

# 가장 큰 이탈율 찾기
max_churn_rate = df['이탈율'].max()

# 가장 큰 이탈율과 다른 이탈율 비교
df['이탈율 비교'] = df['이탈율'].apply(lambda x: '최대 이탈율' if x == max_churn_rate else '다른 이탈율')

# 단계별 이탈율 출력
for i in range(len(df)):
    step = df['단계'][i]
    churn_rate = df['이탈율'][i]
    comparison = df['이탈율 비교'][i]
    print(f'{step}의 이탈율: {churn_rate:.2f}%, {comparison}')
