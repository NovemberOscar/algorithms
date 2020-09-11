data = input()

def solution(data: str):
    """
    5키로 봉지로 나누어 질때까지 3키로 봉지 하나씩 빼면 결과를 구할 수 있다.
    """

    kg = int(data)
    answer = 0

    while True:
        if (kg % 5) == 0:
            answer += kg // 5
            break
        else:
            kg -= 3
            answer += 1

        if kg < 0:
            return -1

    return answer

print(solution(data))