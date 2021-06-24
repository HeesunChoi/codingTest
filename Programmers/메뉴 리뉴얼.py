# https://programmers.co.kr/learn/courses/30/lessons/72411
# 처음부터 모든 경우의 수를 찾는 것이 아닌, 기존의 인풋으로 부터 경우의 수를 세아림

from itertools import combinations as comb

def solution(orders, course):
    answer = []
    dict = {}
    
    for o in orders:
        o = sorted(o)
        for c in course:
            cand = list(comb(o, c))
            for i in cand:
                i = "".join(i)
                if i not in dict:
                    dict[i] = 0
                dict[i] += 1
    
    # print(dict)
    for c in course:
        most_len = 0
        cand = []
        for key, value in dict.items():
            if value < 2:
                continue
            if c == len(key):
                if most_len == value:
                    cand.append(key)
                elif most_len < value:
                    cand = []
                    cand.append(key)
                    most_len = value
        for c in cand:
            answer.append(c)
        

    return sorted(answer)
