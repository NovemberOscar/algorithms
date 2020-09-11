data = input()

def solution(data: str):
    fixed, variable, price = [int(i) for i in data.split()]

    if variable >= price:
        return -1

    point = fixed // (price - variable) + 1
    
    return point


print(solution(data))