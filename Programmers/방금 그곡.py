https://programmers.co.kr/learn/courses/30/lessons/17683

answer = '(None)'
maxtime = -1
def change(m):
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    m = m.replace("A#", 'a')
    
    return m

def solution(m, musicinfos):
    global answer, maxtime
    
    for info in musicinfos:
        info = info.split(",")
        start = int(info[0].split(":")[0])*60 + int(info[0].split(":")[1])
        end = int(info[1].split(":")[0])*60 + int(info[1].split(":")[1])
        title =  info[2]
        melody = change(info[3])
        time = end - start
        total = (melody * time)[:time]

        if change(m) in total and time > maxtime:
            answer = title
            maxtime = time
        
        
    return answer
