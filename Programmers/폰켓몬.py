# https://programmers.co.kr/learn/courses/30/lessons/1845
# 처음 combinations으로 풀어야하는 줄 알았는데, nums의 길이가 10000 까지 가능하다길래, 문제 다시 읽었는데 단순히 set으로 풀이 가능했음

from itertools import combinations
def solution(nums):
    answer = 0
    
    n = len(nums)
    
    # combi = combinations(nums, n/2)
    # m = -1
    # for c in combi:
    #     if len(set(c)) > m:
    #         m = len(set(c))
    
    
    if len(set(nums)) > n/2:
        return n/2
    else:
        return len(set(nums))
    
    return m
