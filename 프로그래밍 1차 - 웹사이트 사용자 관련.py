import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 생성 (가상의 데이터 예시)
data = {
    '단계': ['접속', '상품검색', '상품선택', '장바구니담기', '결제이동'],
    '사용자 수': [10000, 8000, 6000, 4000, 2000]
}

df = pd.DataFrame(data)

# 전환율 계산
df['전환율'] = df['사용자 수'] / df['사용자 수'].iloc[0] * 100

# 단계별 이탈률 계산
df['이탈률'] = 100 - df['전환율'].cumsum()

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

# 단계별 이탈률 시각화
plt.figure(figsize=(8, 6))
plt.plot(df['단계'], df['이탈률'], marker='o')
plt.xlabel('단계')
plt.ylabel('이탈률 (%)')
plt.title('단계별 이탈률')
plt.grid(True)
plt.show()
