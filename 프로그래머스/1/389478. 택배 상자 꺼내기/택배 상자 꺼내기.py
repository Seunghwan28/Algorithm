def solution(n, w, num):
    answer = 0
    
    # 1. num이 위치한 '줄(row)'과 '가로 위치(col)' 계산 (0부터 시작하는 인덱스 기준)
    target_row = (num - 1) // w
    
    # 짝수 줄(0, 2...)은 왼쪽->오른쪽, 홀수 줄(1, 3...)은 오른쪽->왼쪽
    if target_row % 2 == 0:
        col = (num - 1) % w
    else:
        col = w - 1 - ((num - 1) % w)
    
    # 2. 현재 층부터 꼭대기 층까지 반복하며 확인
    # 전체 층 수 (0부터 시작)
    max_row = (n - 1) // w
    
    for row in range(target_row, max_row + 1):
        # 해당 줄(row)의 같은 열(col)에 있는 상자 번호 계산
        if row % 2 == 0:
            box_num = row * w + col + 1
        else:
            box_num = row * w + (w - 1 - col) + 1
            
        # 그 위치의 상자 번호가 n보다 작거나 같으면 꺼낼 상자임
        if box_num <= n:
            answer += 1
            
    return answer