#https://programmers.co.kr/learn/courses/30/lessons/12930
#테스트 케이스만 보고 코드를 작성하면 안되고
#문제를 똑바로 읽도록!!

def solution(s):
    answer = ''
    
    s = s.split(" ")
    # print(s)
    
    for ss in s:
        for idx, sss in enumerate(ss):
            if idx % 2 == 0:
                answer += sss.upper()
            else:
                answer += sss.lower()
        answer += " "
    
    return answer[:len(answer)-1]
[출처] 이상한 문자 만들기|작성자 hsssy01
