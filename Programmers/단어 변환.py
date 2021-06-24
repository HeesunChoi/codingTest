# https://programmers.co.kr/learn/courses/30/lessons/43163

import copy
answer = int(1e9)
def find(current, left_words):
    cands = []
    for w in left_words:
        count = 0
        for i in range(len(w)):
            if w[i] != current[i]:
                count += 1
        if count == 1:
            cands.append(w)
            
    return cands

def dfs(current, time, target, left_words):
    global answer
    # print(current, time, target, left_words)
    if current == target:
        answer = min(time, answer)
        return
    else:
        cands = find(current, left_words) # 한 단어만 다른애들 목록
        for w in cands: # 한 단어에 대해서 current 로 바꿔주고 다시 dfs 부르기
            sub_left = copy.deepcopy(left_words)
            sub_left.remove(w)
            dfs(w, time+1, target, sub_left)
                    

def solution(begin, target, words):
    if target not in words:
        return 0
    
    dfs(begin, 0, target, words)
    
    
    
    return answer
