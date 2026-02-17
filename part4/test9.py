import sys

input = sys.stdin.read
data = input().split()

T = int(data[0])
results = []

for i in range(1, T + 1):
    N = int(data[i])
    
    # 1. 1부터 N까지의 모든 홀수 개수
    total_odds = (N + 1) // 2
    
    # 2. 3j + 1 > N 을 만족하는 홀수 j의 개수 구하기
    # 반대로 3j + 1 <= N 을 만족하는 j의 최대값 K
    K = (N - 1) // 3
    # 1부터 K까지의 홀수 개수
    not_satisfying_odds = (K + 1) // 2
    
    # 3. 전체 홀수 - (만족하지 않는 홀수) = (3j + 1 > N 인 홀수 개수)
    count_condition = total_odds - not_satisfying_odds
    
    # 4. 기존 코드의 로직대로 count_condition에 다시 total_odds를 더함
    ans = count_condition + total_odds
    results.append(str(ans))

sys.stdout.write("\n".join(results) + "\n")