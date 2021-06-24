# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total):
        if total % i == 0:
            a = total // i
            b = i
            if (a-2)*(b-2) == yellow:
                return [a, b]
    
    
    return answer
